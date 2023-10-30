from classes_c import *
class AddPlayerWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.team_manager = TeamManager()
        self.player = Player

    def init_ui(self):
        self.setWindowTitle("Add Player")
        self.setGeometry(100, 100, 300, 200)

        self.name_label = QtWidgets.QLabel("Name:")
        self.name_input = QtWidgets.QLineEdit()

        self.surname_label = QtWidgets.QLabel("Surname:")
        self.surname_input = QtWidgets.QLineEdit()

        self.team_label = QtWidgets.QLabel("Team:")
        self.team_input = QtWidgets.QComboBox()
        # Get team names from teams.csv file
        with open('teams.csv', mode='r') as teams_file:
            reader = csv.reader(teams_file)
            teams = [row[0] for row in reader]

        teams.insert(0, 'Free Player')
        self.team_input.addItems(teams)

        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_button_clicked)

        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(self.surname_label, 1, 0)
        layout.addWidget(self.surname_input, 1, 1)
        layout.addWidget(self.team_label, 2, 0)
        layout.addWidget(self.team_input, 2, 1)
        layout.addWidget(self.ok_button, 3, 0)
        layout.addWidget(self.cancel_button, 3, 1)

        self.setLayout(layout)

    def ok_button_clicked(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        if not name:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Please enter a player name')
            return
        if not surname:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Please enter a surname name')
            return

        self.player = Player(name, surname)
        self.team_manager.add_player(self.player)

        team_name = self.team_input.currentText()
        if team_name == 'FreePlayer':
            QtWidgets.QMessageBox.information(self, 'New Player', f"{name} was added as a free player.")
            self.accept()
        else:
            self.team_manager.assign_player_to_team(self.player, team_name)
            QtWidgets.QMessageBox.information(self, 'New Player', f"{name} was added to team: {team_name}")
            self.accept()
