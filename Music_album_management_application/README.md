This program is a music album management application designed with PyQt6. It enables users to perform the following actions:

1. **Create a new music album**: Users can add albums with details such as album title, artist, and songs through the `CreateWindow` dialog.

2. **Delete an existing album**: The `DeleteWindow` dialog allows users to select and remove an album from the music library.

3. **Manage albums**: Users can manage individual albums, including adding new songs, deleting songs, and editing album or artist information via the `ManageWindow` dialog.

4. **Display album information**: There are two options for displaying album details. Users can display the details of a single selected album or all albums in the library.

The `MainWindow` serves as the central interface, offering buttons to invoke each action and an output area to display information or confirmations. The `MusicLibrary` class is responsible for handling the loading and saving of album data to and from a JSON file, adding and removing albums, and managing the songs within those albums.

Each dialog (`CreateWindow`, `DeleteWindow`, `ManageWindow`) is connected to the corresponding buttons in the main window, and they interact with the `MusicLibrary` instance to perform operations. After each operation, the application updates the music library and, where necessary, saves the changes to the JSON file to persist the data between sessions.

The `Album` class encapsulates the properties of a music album, including its title, artist, and a list of songs. The `Song` class represents individual songs with a title and duration. The `MusicLibrary` class manages a collection of `Album` instances, offering methods to manipulate and retrieve album data.

This application provides a simple yet functional interface for managing a collection of music albums, streamlining the process of organizing a music library.
