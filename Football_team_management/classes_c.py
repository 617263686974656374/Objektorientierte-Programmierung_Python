import os
import csv
from PyQt5 import QtWidgets
class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return f"{self.name}: {', '.join(str(player) for player in self.players)}"


class TeamManager:
    def __init__(self):
        self.teams = []
        self.players = []
        self.team_players = {}

        # Load existing players from file or create new file if it doesn't exist
        if os.path.exists('players.csv'):
            with open('players.csv', mode='r') as players_file:
                reader = csv.reader(players_file)
                for row in reader:
                    player = Player(row[0], row[1])
                    self.players.append(player)
        else:
            with open('players.csv', mode='w', newline='') as players_file:
                pass  # create empty file

        # Load existing teams from file or create new file if it doesn't exist
        if os.path.exists('teams.csv'):
            with open('teams.csv', mode='r') as teams_file:
                reader = csv.reader(teams_file)
                for row in reader:
                    team = Team(row[0])
                    self.teams.append(team)
        else:
            with open('teams.csv', mode='w', newline='') as teams_file:
                pass  # create empty file

        # Load existing team players from file or create new file if it doesn't exist
        if os.path.exists('team_players.csv'):
            with open('team_players.csv', mode='r') as team_players_file:
                reader = csv.reader(team_players_file)
                for row in reader:
                    team_name = row[0]
                    player_name = row[1]
                    player = None
                    for p in self.players:
                        if str(p) == player_name:
                            player = p
                            break
                    if player:
                        if team_name not in self.team_players:
                            self.team_players[team_name] = []
                        self.team_players[team_name].append(player)
        else:
            with open('team_players.csv', mode='w', newline='') as team_players_file:
                pass  # create empty file

    def add_player(self, player):
        self.players.append(player)
        with open('players.csv', mode='a', newline='') as players_file:
            writer = csv.writer(players_file)
            writer.writerow([player.first_name, player.last_name])

    def add_team(self, team):
        self.teams.append(team)
        with open('teams.csv', mode='a', newline='') as teams_file:
            writer = csv.writer(teams_file)
            writer.writerow([team.name])

    def assign_player_to_team(self, player, team_name):
        team = next((t for t in self.teams if t.name == team_name), None)
        if team:
            team.add_player(player)
            if team.name not in self.team_players:
                self.team_players[team.name] = []
            self.team_players[team.name].append(player)
            with open('team_players.csv', mode='a', newline='') as team_players_file:
                writer = csv.writer(team_players_file)
                writer.writerow([team.name, player.first_name, player.last_name])
        else:
            QtWidgets.QMessageBox.warning(None, 'Error', f"No such team found: {team_name}")

    def display_teams(self):
        return self.teams

    def display_team_players(self, team_name):
        if team_name in self.team_players:
            players = self.team_players[team_name]
            if players:
                print(f"Players in team {team_name}:")
                for player in players:
                    print(player)
            else:
                print(f"No players in team {team_name}.")
        else:
            print(f"Team {team_name} not found.")

