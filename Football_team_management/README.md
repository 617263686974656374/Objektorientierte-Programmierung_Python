This program is a football team management application using PyQt5 for the graphical user interface. The application's main functions include:

1. **Adding teams and players**: Users can input new teams and players into the system via dialog windows (`AddTeamWin` and `AddPlayerWindow`).

2. **Displaying players and teams**: It lists all players, including those not assigned to any team, and displays all teams.

3. **Editing teams and players**: Users can swap players between teams or delete them from the system.

4. **Data management**: The program reads from and writes to CSV files to persistently store the information about teams and players (`players.csv`, `teams.csv`, `team_players.csv`).

5. **User Interaction**: It provides a straightforward interface with buttons to perform all actions and input dialogs to capture user inputs.

The application initializes with a `MainWindow`, which contains buttons for each action (adding, displaying, deleting). Each button is connected to a function that opens the corresponding dialog or performs the specified action. The `TeamManager` class is responsible for managing the teams and players, including adding new entries and handling CSV file operations.

The program starts by running the `run_interface()` function from the `MainWindow_c` module, which sets up the `QApplication` and the `MainWindow` and enters the application's main loop. The application's logic is split across multiple modules, with the `classes_c` module defining the `Player`, `Team`, and `TeamManager` classes, and other modules like `addTeamWindow_c` and `addPlayerWindow_c` defining the dialog windows for adding new teams and players, respectively.
