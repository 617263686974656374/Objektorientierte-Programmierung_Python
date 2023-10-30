from Classes_c import *


class ManageWindow(QDialog):
    def __init__(self, library):
        super().__init__()
        self.library = library
        self.libraryx = MusicLibrary.load_albums_from_file()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Manage album")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.album_combo_box = QComboBox()
        self.album_combo_box.addItem("Choose album")

        albums = self.library.get_albums()
        for album in albums:
            self.album_combo_box.addItem(album)

        layout.addWidget(self.album_combo_box)

        self.add_button = QPushButton("Add song")
        self.add_button.clicked.connect(self.add_button_clicked)
        layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete song")
        self.delete_button.clicked.connect(self.delete_button_clicked)
        layout.addWidget(self.delete_button)

        self.edit_album_title_button = QPushButton("Edit album title")
        self.edit_album_title_button.clicked.connect(self.edit_album_title_button_clicked)
        layout.addWidget(self.edit_album_title_button)

        self.edit_artist_button = QPushButton("Edit artist")
        self.edit_artist_button.clicked.connect(self.edit_artist_button_clicked)
        layout.addWidget(self.edit_artist_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def update_library(self):
        self.libraryx = MusicLibrary.load_albums_from_file()

    def add_button_clicked(self):
        selected_album_title = self.album_combo_box.currentText()
        selected_album = self.library.get_one_album(selected_album_title)

        if selected_album:
            while True:
                song_name, ok = QInputDialog.getText(self, 'Add song', 'Enter song name:')
                if ok and song_name.strip():  # kontrola, či je zadaný názov piesne
                    break
                else:
                    msg_box = QMessageBox()
                    msg_box.setText("Song name cannot be empty!")
                    msg_box.exec()

            while True:
                song_duration, ok = QInputDialog.getInt(self, 'Add song', 'Enter song duration (seconds):')
                if ok:
                    break
                else:
                    msg_box = QMessageBox()
                    msg_box.setText("Please enter a valid integer!")
                    msg_box.exec()

            new_song = Song(song_name, song_duration)
            selected_album.add_song(new_song)
            QMessageBox.information(self, "Info", f"Song '{song_name}' with duration {song_duration} seconds was added to the album '{selected_album_title}'.")

            self.update_library()
        else:
            QMessageBox.warning(self, "Warning", "No album selected.")
        MusicLibrary.save_albums_to_file(self.library)  # Save the updated library to file

    def delete_button_clicked(self):
        selected_album_title = self.album_combo_box.currentText()
        selected_album = self.library.get_one_album(selected_album_title)

        if selected_album and selected_album.songs:
            msg_box = QMessageBox()
            msg_box.setText("Select a song to delete:")
            combo_box = QComboBox()
            songs = [song.title for song in selected_album.songs]
            combo_box.addItems(songs)
            msg_box.layout().addWidget(combo_box)
            ok_button = msg_box.addButton("OK", QMessageBox.ButtonRole.AcceptRole)
            msg_box.exec()

            if msg_box.clickedButton() == ok_button:
                selected_song_title = combo_box.currentText()
                for song in selected_album.songs:
                    if song.title == selected_song_title:
                        selected_album.remove_song(song)
                        QMessageBox.information(self, "Info",
                                                f"Song '{selected_song_title}' was deleted from the album '{selected_album_title}'.")
                        MusicLibrary.save_albums_to_file(self.library)  # Save the updated library to file
                        return

                QMessageBox.warning(self, "Warning",
                                    f"Song '{selected_song_title}' not found in the album '{selected_album_title}'.")
            else:
                QMessageBox.warning(self, "Warning", "Song deletion cancelled.")
        else:
            QMessageBox.warning(self, "Warning", "No album selected or the selected album has no songs.")

    def edit_album_title_button_clicked(self):
        selected_album_title = self.album_combo_box.currentText()
        selected_album = self.library.get_one_album(selected_album_title)

        if selected_album:
            new_title, ok = QInputDialog.getText(self, 'Edit album title', 'Enter new album title:')
            if ok and new_title.strip():
                selected_album.title = new_title
                self.album_combo_box.setItemText(self.album_combo_box.currentIndex(), new_title)
                QMessageBox.information(self, "Info", f"Album '{new_title}' was renamed from the album '{selected_album_title}'.")
                self.update_library()
            else:
                QMessageBox.warning(self, "Warning", "New album title cannot be empty")
        else:
            QMessageBox.warning(self, "Warning", "No album selected")
        MusicLibrary.save_albums_to_file(self.library)  # Save the updated library to file
    def edit_artist_button_clicked(self):
        selected_album_title = self.album_combo_box.currentText()
        selected_album = self.library.get_one_album(selected_album_title)

        if selected_album:
            new_artist, ok = QInputDialog.getText(self, 'Edit artist', 'Enter new artist:')
            if ok and new_artist.strip():
                selected_album.artist = new_artist
                QMessageBox.information(self, "Info",
                                        f"Artist '{new_artist}' was renamed from the Artist '{selected_album_title}'.")
                self.update_library()
            else:
                QMessageBox.warning(self, "Warning", "New artist cannot be empty")
        else:
            QMessageBox.warning(self, "Warning", "No album selected")
        MusicLibrary.save_albums_to_file(self.library)  # Save the updated library to file
