This program is a simple PyQt6 application that allows users to gather information about the system they are running the application on, and either display it, save it to a CSV file, or load it from a CSV file. The key features of the application include:

1. **User Interface**: The application has a basic user interface with checkboxes to select the type of information to be saved or displayed (`platform_info`, `sys_info`, `architecture_info`), a preview button to show the selected information, save and upload buttons to handle CSV files, and a label to display information (`info_preview`).

2. **Preview Information**: When the "Show preview" button is clicked, the application generates a preview of the selected system information and displays it in the `info_preview` label.

3. **Save Information**: The "Save information" button triggers a file dialog allowing the user to choose a location and filename to save the selected system information as a CSV file.

4. **Load Information**: The "Upload data" button lets the user select a CSV file to load. The contents of the file are then displayed in the `info_preview` label.

5. **System Information**: The information that can be collected includes platform information (like Python version, system platform, and system version), system information (like maximum Unicode size and the path to the interpreter), and architecture information (like architecture, network name, and MAC address).

The `MainWindow` class manages the layout and widgets, as well as the actions triggered by the user interface. The `preview_info` method compiles the selected system information into a string and updates the `info_preview` label with this string. The `save_info` method writes the selected information to a CSV file, and the `load_csv` method reads from a CSV file and displays the contents.

When the application is launched, it creates an instance of `MainWindow` and displays it. The program exits when the user closes the application window.
