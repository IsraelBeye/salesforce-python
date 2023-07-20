# Salesforce Utility Module

This repository contains a Python module that provides utility functions to connect to Salesforce and retrieve data from Salesforce tables. The module utilizes the `simple-salesforce` library to interact with Salesforce's REST API and `pandas` for data manipulation.

## Installation

To use the Salesforce utility module, you need to install the required dependencies. Run the following command to install the necessary packages:

pip install simple-salesforce pandas


## Functions

### `salesforce_table_selectedColumns`

```python
def salesforce_table_selectedColumns(username, password, token_number, table_name, fields, where_arg=None):
    """
    Fetch data from Salesforce table for selected columns.

    Parameters:
        username (str): Salesforce username.
        password (str): Salesforce password.
        token_number (str): Salesforce security token.
        table_name (str): Name of the table in Salesforce.
        fields (list): List of columns needed (e.g., ['col_a', 'col_b']).
        where_arg (str, optional): WHERE clause for filtering data (e.g., "WHERE col_a = 'value'").

    Returns:
        pandas.DataFrame: DataFrame containing the queried data.
    """
### `salesforce_table`
def salesforce_table(table_name, username, password, token_number, where_arg=None):
    """
    Fetch data from Salesforce table for all columns.

    Parameters:
        table_name (str): Name of the table in Salesforce.
        username (str): Salesforce username.
        password (str): Salesforce password.
        token_number (str): Salesforce security token.
        where_arg (str, optional): WHERE clause for filtering data (e.g., "WHERE col_a = 'value'").

    Returns:
        pandas.DataFrame: DataFrame containing the queried data.
    """
# Usage
To use the Salesforce utility module, follow these steps:

1. Import the module in your Python script:


from salesforce_utils import salesforce_table_selectedColumns, salesforce_table
# Example 1: Fetch data from 'Resource_Assignment__c' table with specific columns
username = "your_salesforce_username"
password = "your_salesforce_password"
security_token = "your_salesforce_security_token"
table_name = "Opportunity"
columns = ['Name', 'Status', 'Start_Date__c']
data = salesforce_table_selectedColumns(username, password, security_token, table_name, columns)
print(data)

# Example 2: Fetch all data from 'Account' table with optional WHERE clause
username = "your_salesforce_username"
password = "your_salesforce_password"
security_token = "your_salesforce_security_token"
table_name = "Account"
where_clause = "WHERE Industry = 'Technology'"
data = salesforce_table(table_name, username, password, security_token, where_arg=where_clause)
print(data)
Remember to replace your_salesforce_username, your_salesforce_password, and your_salesforce_security_token with your actual Salesforce credentials.

# Contributing
If you have suggestions, bug reports, or would like to contribute to this project, feel free to open an issue or create a pull request.
