from classes_c import *
class AddTeamWin(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.team_manager = TeamManager()
        self.team = Team

    def init_ui(self):
        self.setWindowTitle("Add Team")
        self.setGeometry(100, 100, 300, 200)

        self.club_name_label = QtWidgets.QLabel("Team Name:")
        self.club_name_input = QtWidgets.QLineEdit()

        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_button_clicked)

        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.club_name_label, 0, 0)
        layout.addWidget(self.club_name_input, 0, 1)

        layout.addWidget(self.ok_button, 1, 0)
        layout.addWidget(self.cancel_button, 1, 1)

        self.setLayout(layout)

    def ok_button_clicked(self):
        club_name = self.club_name_input.text()
        if not club_name:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Please enter a Club name')
            return

        club_n = next((t for t in self.team_manager.teams if t.name == club_name), None)
        if club_n:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Selected team already exist')
            return

        team = Team(club_name)
        self.team_manager.add_team(team)

        QtWidgets.QMessageBox.information(self, 'New Team', f"{club_name} was created")
        self.accept()
