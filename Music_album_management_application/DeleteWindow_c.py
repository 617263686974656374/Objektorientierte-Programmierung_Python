from Classes_c import *


class DeleteWindow(QDialog):
    def __init__(self, library):
        super().__init__()
        self.library = library
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Delete album")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.album_combo_box = QComboBox()
        self.album_combo_box.addItem("Choose album")

        albums = self.library.get_albums()
        for album in albums:
            self.album_combo_box.addItem(album)

        layout.addWidget(self.album_combo_box)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_button_clicked)
        layout.addWidget(self.delete_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def delete_button_clicked(self):
        selected_album = self.album_combo_box.currentText()
        if selected_album != "Choose album":
            self.library.remove_album(selected_album)
            self.accept()
        else:
            QMessageBox.warning(self, "Warning", "Please select an album to delete.")
            self.reject()
