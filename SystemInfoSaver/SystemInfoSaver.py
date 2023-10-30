import sys
import platform
import csv
import uuid, re
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QLabel, QPushButton, QFileDialog, QScrollArea, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.platform_info = QCheckBox("Platform information")
        self.sys_info = QCheckBox("System information")
        self.architecture_info = QCheckBox("Information about platform architecture")
        self.preview_button = QPushButton("Show preview")
        self.preview_button.clicked.connect(self.preview_info)
        self.save_button = QPushButton("Save information")
        self.save_button.clicked.connect(self.save_info)
        self.load_button = QPushButton("Upload data")
        self.load_button.clicked.connect(self.load_csv)

        layout.addWidget(QLabel("Select the information you want to save:"))
        layout.addWidget(self.platform_info)
        layout.addWidget(self.sys_info)
        layout.addWidget(self.architecture_info)
        layout.addWidget(self.preview_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)

        self.info_preview = QLabel()
        layout.addWidget(self.info_preview)

        self.setLayout(layout)

    def preview_info(self):
        preview_text = ""

        if self.platform_info.isChecked():
            preview_text += "Platform information:\n"
            preview_text += "Python version: " + platform.python_version() + "\n"
            preview_text += "System platform: " + platform.system() + "\n"
            preview_text += "System version: " + platform.version() + "\n\n"

        if self.sys_info.isChecked():
            preview_text += "System information:\n"
            preview_text += "Maximum Unicode size: " + str(sys.maxunicode) + "\n"
            preview_text += "The path to the interpreter: " + sys.executable + "\n\n"

        if self.architecture_info.isChecked():
            preview_text += "Information about platform architecture:\n"
            preview_text += "Architecture: " + str(platform.architecture()) + "\n"
            preview_text += "Network name: " + platform.node() + "\n"
            preview_text += "Mac address: " + (':'.join(re.findall('..', '%012x' % uuid.getnode()))) + "\n\n"


        self.info_preview.setText(preview_text)

    def save_info(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Uložiť informácie", "", "CSV súbory (*.csv)")

        if file_path:
            with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
                csv_writer = csv.writer(csvfile)

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                csv_writer.writerow(["Date and time of storage:", now])
                csv_writer.writerow([""])

                if self.platform_info.isChecked():
                    csv_writer.writerow(["Platform information"])
                    csv_writer.writerow(["Python version:", platform.python_version()])
                    csv_writer.writerow(["System platform:", platform.system()])
                    csv_writer.writerow(["System version:", platform.version()])
                    csv_writer.writerow([""])

                if self.sys_info.isChecked():
                    csv_writer.writerow(["System information"])
                    csv_writer.writerow(["Maximum Unicode size:", sys.maxunicode])
                    csv_writer.writerow(["The path to the interpreter:", sys.executable])
                    csv_writer.writerow([""])

                if self.architecture_info.isChecked():
                    csv_writer.writerow(["Information about platform architecture:"])
                    csv_writer.writerow(["Architecture:", platform.architecture()])
                    csv_writer.writerow(["Network name:", platform.node()])
                    csv_writer.writerow(["Mac address:", (':'.join(re.findall('..', '%012x' % uuid.getnode())))])
                    csv_writer.writerow([""])
            # Pridajte ďalšie možnosti, ak chcete uložiť ďalšie informácie
    def load_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Načítať CSV súbor", "", "CSV súbory (*.csv)")

        if file_path:
            with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
                csv_reader = csv.reader(csvfile)
                loaded_text = ""
                for row in csv_reader:
                    loaded_text += ", ".join(row) + "\n"

            self.info_preview.setText(loaded_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
