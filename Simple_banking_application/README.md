This program is a simple banking application with a graphical user interface (GUI) developed using PyQt6. The application facilitates basic bank account operations, including:

- **Creating accounts**: Users can create a new bank account by providing a name, surname, and initial deposit amount.
- **Deleting accounts**: Users can delete an existing account from the bank's records.
- **Withdrawing money**: Account holders can withdraw money from their accounts, provided they have sufficient funds.
- **Depositing money**: Allows account holders to deposit money into their accounts.
- **Displaying account information**: The application can display information for individual accounts or all accounts together.

The `MainWindow` serves as the main interface window, offering buttons for each banking operation. Clicking a button opens a corresponding dialog (`AccountWindow`, `DeleteWindow`, `WithdrawWindow`, `DepositWindow`, `DisplayWindow`) that handles the selected action.

The `Function` class is a utility class that provides static methods for handling accounts, such as loading and saving account data from/to a JSON file, creating, deleting, depositing, and withdrawing money from accounts, and displaying account information.

The program begins execution from the `MainWindow` class, which sets up the main application window and loads existing account data from a file. Each window class (`AccountWindow`, `DeleteWindow`, `WithdrawWindow`, `DepositWindow`, `DisplayWindow`) is responsible for managing user inputs for their respective operations and interacting with the `Function` class to perform the logic.

When a user performs an action, such as creating or deleting an account, the `Function` class updates the internal account list and saves the changes to the JSON file to persist the data. The application also provides feedback to the user with messages indicating the success or failure of their operations.
