from Classes_c import *


class CreateWindow(QDialog):
    def __init__(self, library):
        super().__init__()
        self.library = library
        self.current_album = Album('')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Create album")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Album name input
        hbox = QHBoxLayout()
        self.label = QLabel("Album name:")
        hbox.addWidget(self.label)
        self.album_input = QLineEdit()
        hbox.addWidget(self.album_input)
        layout.addLayout(hbox)

        # Artist input
        hbox = QHBoxLayout()
        self.label = QLabel("Artist:")
        hbox.addWidget(self.label)
        self.artist_input = QLineEdit()
        hbox.addWidget(self.artist_input)
        layout.addLayout(hbox)

        # Display album, artist, and song info
        self.info_label = QLabel()
        layout.addWidget(self.info_label)

        self.add_button = QPushButton("Add song")
        self.add_button.clicked.connect(self.add_song)
        layout.addWidget(self.add_button)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_button_clicked)
        layout.addWidget(self.save_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def update_info_label(self):
        album_title = self.current_album.title if self.current_album.title else "N/A"
        album_duration = self.current_album.get_duration()
        artist = self.current_album.artist if self.current_album.artist else "N/A"

        song_list = ""
        if self.current_album.songs:
            for song in self.current_album.songs:
                song_title = song.title
                song_duration = song.get_duration()
                song_list += f"{song_title} ({song_duration})\n"
        else:
            song_list = "No songs added."

        self.info_label.setText(
            f"Album: {album_title} ({album_duration})\n"
            f"Artist: {artist}\n"
            f"Songs:\n{song_list}"
        )


    def check_input(self):
        if not self.album_input.text():
            msg_box = QMessageBox()
            msg_box.setText("Please enter an album name!")
            msg_box.exec()
            return False
        if not self.artist_input.text():
            msg_box = QMessageBox()
            msg_box.setText("Please enter an artist name!")
            msg_box.exec()
            return False
        return True

    def add_song(self):
        if self.check_input():
            self.current_album.title = self.album_input.text().strip()
            self.current_album.artist = self.artist_input.text().strip()
            while True:
                song_name, ok = QInputDialog.getText(self, 'Add song', 'Enter song name:')
                if ok and song_name.strip():
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

            song = Song(song_name, song_duration)
            self.current_album.add_song(song)
            self.update_info_label()

    def save_button_clicked(self):
        if self.check_input():
            album_name = self.album_input.text().strip()
            artist_name = self.artist_input.text().strip()
            self.current_album.title = album_name
            self.current_album.artist = artist_name
            self.library.add_album(self.current_album)
            self.current_album = Album('')  # Reset the current album
            self.update_info_label()
            self.accept()
