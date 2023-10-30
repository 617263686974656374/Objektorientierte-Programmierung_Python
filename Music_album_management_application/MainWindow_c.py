from CreateWindow_c import *
from DeleteWindow_c import *
from ManageWindow_c import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.library = MusicLibrary.load_albums_from_file()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Music manager")
        layout = QVBoxLayout()

        btn = QPushButton("Create album")
        btn.clicked.connect(self.create_album_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Delete album")
        btn.clicked.connect(self.delete_album_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Manage album")
        btn.clicked.connect(self.manage_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Display one album")
        btn.clicked.connect(self.display_one_album_button_clicked)
        layout.addWidget(btn)

        btn = QPushButton("Display all albums")
        btn.clicked.connect(self.display_all_albums_button_clicked)
        layout.addWidget(btn)


        self.output = QPlainTextEdit()
        layout.addWidget(self.output)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def create_album_button_clicked(self):
        library = MusicLibrary.load_albums_from_file()
        dialog = CreateWindow(library)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            MusicLibrary.save_albums_to_file(library)
            self.update_library()

    def delete_album_button_clicked(self):
        self.output.clear()
        dialog = DeleteWindow(self.library)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            MusicLibrary.save_albums_to_file(self.library)  # Zmena na správny názov funkcie
            self.output.appendPlainText(f'Album deleted!')
        else:
            self.output.appendPlainText(f'Album deletion cancelled.')

    def manage_button_clicked(self):
        dialog = ManageWindow(self.library)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            MusicLibrary.save_albums_to_file(self.library)
            self.update_library()

    def display_one_album_button_clicked(self):
        msg_box = QMessageBox()
        msg_box.setText("Select an album to display:")
        combo_box = QComboBox()
        albums = self.library.get_albums()  # Zmena na self.library
        combo_box.addItems(albums)
        msg_box.layout().addWidget(combo_box)
        ok_button = msg_box.addButton("OK", QMessageBox.ButtonRole.AcceptRole)
        msg_box.exec()

        if msg_box.clickedButton() == ok_button:
            selected_album = combo_box.currentText()
            album = self.library.get_one_album(selected_album)  # Zmena na self.library
            if album and album.songs:
                self.output.clear()
                self.output.appendPlainText(
                    f"Album: {album.title}\nArtist: {album.artist}\nDuration: {album.get_duration()}\n")
                for song in album.songs:
                    self.output.appendPlainText(f"\nSong: {song.title}\nDuration: {song.get_duration()}")
            elif not album:
                self.output.appendPlainText(f"Album '{selected_album}' not found.")
            else:
                self.output.appendPlainText(f"Album '{selected_album}' is without song.")

    def display_all_albums_button_clicked(self):
        self.output.clear()
        for album in self.library.albums:
            self.output.appendPlainText(
                f"Album: {album.title}\nArtist: {album.artist}\nDuration: {album.get_duration()}\n")

    def update_library(self):
        self.library = MusicLibrary.load_albums_from_file()

