# Fund Transfer Web App

This is a Django web application that handles fund transfers between two accounts. The app supports importing a list of accounts with opening balances from a CSV file, querying these accounts, and transferring funds between any two accounts.

## Features


- Import accounts from CSV or XLSX files.
- List all accounts.
- Get account information.
- Transfer funds between two accounts.
- Error handling already added in every part of the project.

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (default) or any other preferred database

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/fund-transfer-web-app.git
    cd fund-transfer-web-app
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Import Accounts

1. The project will navigate automatically to "import" template if there is no data still saved in database.
2. Upload a CSV file with accounts data. The CSV file should have the following format:

    ```csv
    account_number,account_name,balance
    123456,Test Account 1,1000.00
    789012,Test Account 2,2000.00
    ```

### List Accounts

1. The project will navigate automatically to "list accounts" template when start running the application if there is data already found in database.
2. View the list of all imported accounts.

### View Account Details

1. There is a "Show Details" button for every account in "list accounts" table shows the info of the account.

### Transfer Funds

1. There is a "Transfer Funds" button for every account in "list accounts" table to choose this account as the source account you want to transfer this fund from.
2. After navigating to the "transfer funds" template select destination account from the dropdown and enter the amount to transfer.
3. Click the "Transfer" button to complete the transaction.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test accounts
