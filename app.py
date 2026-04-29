from datetime import datetime
from pathlib import Path
import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = "replace-this-with-a-random-secret-key"

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database.db"
TRANSACTION_TYPES = ("income", "expense")


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
        """
    )
    connection.commit()
    connection.close()


def validate_transaction(form_data):
    errors = []

    transaction_type = form_data.get("type", "").strip().lower()
    amount_text = form_data.get("amount", "").strip()
    category = form_data.get("category", "").strip()
    date_text = form_data.get("date", "").strip()
    description = form_data.get("description", "").strip()

    if transaction_type not in TRANSACTION_TYPES:
        errors.append("Please choose income or expense.")

    try:
        amount = float(amount_text)
        if amount <= 0:
            errors.append("Amount must be greater than zero.")
    except ValueError:
        amount = None
        errors.append("Amount must be a valid number.")

    if not category:
        errors.append("Category is required.")

    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        errors.append("Date must be in YYYY-MM-DD format.")

    return errors, {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "date": date_text,
        "description": description,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    init_db()

    if request.method == "POST":
        errors, transaction = validate_transaction(request.form)

        if errors:
            for error in errors:
                flash(error, "error")
        else:
            connection = get_db_connection()
            connection.execute(
                """
                INSERT INTO transactions (type, amount, category, date, description)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    transaction["type"],
                    transaction["amount"],
                    transaction["category"],
                    transaction["date"],
                    transaction["description"],
                ),
            )
            connection.commit()
            connection.close()
            flash("Transaction added successfully.", "success")
            return redirect(url_for("index"))

    connection = get_db_connection()
    transactions = connection.execute(
        "SELECT * FROM transactions ORDER BY date DESC, id DESC"
    ).fetchall()

    totals = connection.execute(
        """
        SELECT
            COALESCE(SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END), 0) AS income,
            COALESCE(SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END), 0) AS expenses
        FROM transactions
        """
    ).fetchone()

    monthly_summary = connection.execute(
        """
        SELECT
            strftime('%Y-%m', date) AS month,
            COALESCE(SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END), 0) AS income,
            COALESCE(SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END), 0) AS expenses
        FROM transactions
        GROUP BY month
        ORDER BY month DESC
        """
    ).fetchall()
    connection.close()

    total_income = totals["income"]
    total_expenses = totals["expenses"]
    balance = total_income - total_expenses

    return render_template(
        "index.html",
        transactions=transactions,
        monthly_summary=monthly_summary,
        total_income=total_income,
        total_expenses=total_expenses,
        balance=balance,
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
