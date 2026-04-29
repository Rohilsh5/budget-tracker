# Budget Tracker App

A simple Flask and SQLite web application for tracking income and expenses. The goal of this project is to show practical backend, database, and frontend skills in a clean beginner-friendly codebase.

This project is suitable for a university portfolio because it solves a realistic problem without using unnecessary frameworks or advanced architecture.

## Features

- Add income and expense transactions
- Store each transaction with amount, category, date, and description
- Save data in a local SQLite database
- Display all transactions in a table
- Show total income, total expenses, and current balance
- Show a monthly income and expense summary
- Basic input validation for required fields, date, and amount
- Responsive HTML and CSS layout

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS

## Project Structure

```text
budget-tracker/
|-- app.py
|-- requirements.txt
|-- README.md
|-- database.db
|-- templates/
|   |-- index.html
|-- static/
|   |-- style.css
```

`database.db` is created automatically when the app runs for the first time.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/budget-tracker.git
cd budget-tracker
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Start the Flask app:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Screenshots

Add screenshots here after running the app locally.

Example:

```text
screenshots/homepage.png
screenshots/transactions.png
```

## File Explanation

- `app.py` contains the Flask routes, SQLite database setup, form validation, and summary calculations.
- `requirements.txt` lists the Python packages needed to run the app.
- `templates/index.html` is the main page. It contains the form, balance cards, monthly summary table, and transaction table.
- `static/style.css` controls the visual design and responsive layout.
- `database.db` stores the transaction records locally and is created automatically by the app.

## Suggested Git Workflow

Use multiple commits to make the project history look realistic and easy to review.

```bash
mkdir budget-tracker
cd budget-tracker
git init

python -m venv venv
echo venv/ > .gitignore
echo database.db >> .gitignore
git add .gitignore
git commit -m "initial project setup"

touch app.py requirements.txt README.md
mkdir templates static
touch templates/index.html static/style.css
git add .
git commit -m "created project structure"

git add requirements.txt
git commit -m "added Flask dependency"

git add app.py
git commit -m "added database schema"

git add app.py templates/index.html
git commit -m "implemented transaction form"

git add app.py
git commit -m "added input validation"

git add app.py templates/index.html
git commit -m "displayed transactions and balance"

git add app.py templates/index.html
git commit -m "added monthly summary"

git add static/style.css
git commit -m "styled budget tracker interface"

git add README.md
git commit -m "updated project documentation"
```

## Create a GitHub Repository and Push

1. Create a new repository on GitHub named `budget-tracker`.
2. Do not initialize it with a README because this project already has one.
3. Connect the local project to GitHub:

```bash
git branch -M main
git remote add origin https://github.com/your-username/budget-tracker.git
git push -u origin main
```

Replace `your-username` with your GitHub username.

## Example Commit Messages

- initial project setup
- created project structure
- added Flask dependency
- added database schema
- implemented transaction form
- added input validation
- displayed transactions and balance
- added monthly summary
- styled budget tracker interface
- updated project documentation
- fixed input validation bug
- improved README setup instructions
