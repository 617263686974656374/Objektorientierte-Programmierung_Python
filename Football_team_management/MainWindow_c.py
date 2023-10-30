from addTeamWindow_c import *
from addPlayerWindow_c import *



def read_csv(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        return [row for row in reader]


def show_message_box(title, message):
    message_box = QtWidgets.QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(message)
    message_box.exec_()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.team_manager = TeamManager()

    def init_ui(self):
        self.setWindowTitle("Football Manager")
        self.setGeometry(100, 100, 300, 200)

        self.add_team_button = QtWidgets.QPushButton("Add team")
        self.add_team_button.clicked.connect(self.add_team_button_clicked)

        self.add_player_button = QtWidgets.QPushButton("Add_player")
        self.add_player_button.clicked.connect(self.add_player_button_clicked)

        self.show_players_button = QtWidgets.QPushButton("Show Players")
        self.show_players_button.clicked.connect(self.show_players_button_clicked)

        self.swap_player_button = QtWidgets.QPushButton("Swap players")
        self.swap_player_button.clicked.connect(self.swap_player_button_clicked)

        self.show_all_clubs_button = QtWidgets.QPushButton("Show all teams")
        self.show_all_clubs_button.clicked.connect(self.show_all_clubs_button_clicked)

        self.delete_club_button = QtWidgets.QPushButton("Delete team")
        self.delete_club_button.clicked.connect(self.delete_club_button_clicked)

        self.delete_player_button = QtWidgets.QPushButton("Delete player")
        self.delete_player_button.clicked.connect(self.delete_player_button_clicked)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.add_team_button)
        layout.addWidget(self.add_player_button)
        layout.addWidget(self.swap_player_button)
        layout.addWidget(self.show_players_button)
        layout.addWidget(self.show_all_clubs_button)
        layout.addWidget(self.delete_club_button)
        layout.addWidget(self.delete_player_button)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_team_button_clicked(self):
        dialog = AddTeamWin()
        dialog.exec_()
        self.team_manager = TeamManager()

    def add_player_button_clicked(self):
        dialog = AddPlayerWindow()
        dialog.exec_()
        self.team_manager = TeamManager()

    def show_players_button_clicked(self):
        players = []
        players_list = read_csv('players.csv')
        team_players_list = read_csv('team_players.csv')

        for player_row in players_list:
            for team_player_row in team_players_list:
                if player_row[0] == team_player_row[1] and player_row[1] == team_player_row[2]:
                    players.append((player_row[0], player_row[1], team_player_row[0]))

        # Add players without a team to the list
        for player_row in players_list:
            assigned = False
            for team_player_row in team_players_list:
                if player_row[0] == team_player_row[1] and player_row[1] == team_player_row[2]:
                    assigned = True
                    break
            if not assigned:
                players.append((player_row[0], player_row[1], 'Free Player'))

        # Display players
        if players:
            player_names = "\n".join(f"{player[0]} {player[1]}  ({player[2]})" for player in players)
            show_message_box('Players', player_names)
        else:
            show_message_box('Players', 'No players found')

    def show_all_clubs_button_clicked(self):
        teams_list = read_csv('teams.csv')
        teams = [Team(row[0]) for row in teams_list]

        if teams:
            team_names = "\n".join(str(team) for team in teams)
            show_message_box('Teams', team_names)
        else:
            show_message_box('Teams', 'No teams found')

    def delete_club_button_clicked(self):
        if not self.team_manager.teams:
            QtWidgets.QMessageBox.information(self, 'Teams', 'No teams found')
        else:

            club_name, ok = QtWidgets.QInputDialog.getItem(self, "Delete Club", "Select Club to Delete:",
                                                           [team.name for team in self.team_manager.teams], editable=False)
            if ok and club_name:
                # Remove the team from the list of teams
                team_to_delete = next((team for team in self.team_manager.teams if team.name == club_name), None)
                if team_to_delete:
                    self.team_manager.teams.remove(team_to_delete)

                    # Update the teams.csv file
                    with open('teams.csv', mode='w', newline='') as teams_file:
                        writer = csv.writer(teams_file)
                        for team in self.team_manager.teams:
                            writer.writerow([team.name])

                    # Remove players from the team in team_players.csv
                    with open('team_players.csv', mode='r') as team_players_file:
                        reader = csv.reader(team_players_file)
                        rows_to_keep = [row for row in reader if row[0] != club_name]

                    with open('team_players.csv', mode='w', newline='') as team_players_file:
                        writer = csv.writer(team_players_file)
                        writer.writerows(rows_to_keep)

                    # Remove players from the team in memory
                    players_to_remove = [player for player in self.team_manager.team_players.get(club_name, [])]
                    for player in players_to_remove:
                        self.team_manager.team_players[club_name].remove(player)

                    # Show a message to inform the user
                    QtWidgets.QMessageBox.information(self, 'Club Deleted', f"{club_name} was deleted.")
                else:
                    QtWidgets.QMessageBox.warning(self, 'Error', f"No such team found: {club_name}")

    def delete_player_button_clicked(self):
        if not self.team_manager.players:
            QtWidgets.QMessageBox.information(self, 'Players', 'No players found')
        else:
            player_names = [f"{player.first_name} {player.last_name}" for player in self.team_manager.players]
            player_name, ok = QtWidgets.QInputDialog.getItem(self, "Select Player", "Enter Player Name:", player_names,
                                                             editable=False)
            if ok and player_name:
                with open('players.csv', mode='r') as players_file:
                    players_reader = csv.reader(players_file)
                    players = [row for row in players_reader if f"{row[0]} {row[1]}" != player_name]
                with open('players.csv', mode='w', newline='') as players_file:
                    players_writer = csv.writer(players_file)
                    players_writer.writerows(players)
                with open('team_players.csv', mode='r') as team_players_file:
                    team_players_reader = csv.reader(team_players_file)
                    team_players = [row for row in team_players_reader if f"{row[1]} {row[2]}" != player_name]
                with open('team_players.csv', mode='w', newline='') as team_players_file:
                    team_players_writer = csv.writer(team_players_file)
                    team_players_writer.writerows(team_players)
                QtWidgets.QMessageBox.information(self, 'Delete Player', f"{player_name} was deleted.")
            self.team_manager = TeamManager()

    def swap_player_button_clicked(self):
        # Load player names and current team names from team_players.csv
        with open('team_players.csv', mode='r', newline='') as team_players_file:
            reader = csv.reader(team_players_file)
            player_names = [(f"{row[1]} {row[2]}", row[0]) for row in reader if len(row) == 3]

        if not player_names:
            QtWidgets.QMessageBox.information(self, 'Swap Players', 'No players found')
            return

        # Get the player and their current team from user input
        player_name, player_team = QtWidgets.QInputDialog.getItem(self, "Swap Players", "Select Player to Swap:",
                                                                  [f"{name} ({team})" for name, team in player_names],
                                                                  editable=False)
        if not player_name or not player_team:
            return
        # Get the target team from user input
        target_team_names = [team.name for team in self.team_manager.teams if team.name != player_team]
        if not target_team_names:
            QtWidgets.QMessageBox.warning(self, 'Swap Players', f"No other teams found to move {player_name} to.")
            return
        target_team, ok = QtWidgets.QInputDialog.getItem(self, "Swap Players", "Select Target Team:", target_team_names,
                                                         editable=False)
        if not ok or not target_team:
            return

        # Find the player and their current team
        player_found = False
        with open('team_players.csv', mode='r', newline='') as team_players_file:
            reader = csv.reader(team_players_file)
            lines = list(reader)
            for i in range(len(lines)):
                row = lines[i]
                if len(row) != 3:
                    continue
                if f"{row[1]} {row[2]}" == player_name and row[0] == player_team:
                    player_found = True
                    # Remove the player from the current team
                    lines.pop(i)
                    for team in self.team_manager.teams:
                        if team.name == player_team:
                            team.remove_player(row[1], row[2])
                            break
                    # Remove the player from the team_players dictionary
                    if player_team in self.team_manager.team_players:
                        self.team_manager.team_players[player_team] = [p for p in
                                                                       self.team_manager.team_players[player_team] if
                                                                       f"{p.first_name} {p.last_name}" != player_name]
                    # Assign the player to the target team
                    players = [player for player in self.team_manager.players if any(
                        team.name == player_team for team in self.team_manager.teams if player in team.players)]
                    if not players:
                        QtWidgets.QMessageBox.warning(self, 'Swap Players', f"No players found in team {player_team}.")
                        return
                    player, ok = QtWidgets.QInputDialog.getItem(self, "Swap Players", "Select Player:",
                                                                [f"{p.first_name} {p.last_name}" for p in players],
                                                                editable=False)
                    if not ok or not player:
                        return
                    for target in self.team_manager.teams:
                        if target.name == target_team:
                            for p in players:
                                if f"{p.first_name} {p.last_name}" == player:
                                    target.add_player(p)
                                    self.team_manager.team_players.setdefault(target_team, []).append(p)
                                    # Append the updated player record to lines
                                    lines.append([target_team, p.first_name, p.last_name])
                                    break
                            break
            # Update the team_players.csv file if player is found
            if player_found:
                with open('team_players.csv', mode='w', newline='') as team_players_file:
                    writer = csv.writer(team_players_file)
                    writer.writerows(lines)
                QtWidgets.QMessageBox.information(self, 'Swap Players',
                                                  f"{player_name} was moved from {player_team} to {target_team}.")
            else:
                QtWidgets.QMessageBox.warning(self, 'Swap Players', 'No such player found.')
                return

    def cancel_button_clicked(self):
        self.reject()
