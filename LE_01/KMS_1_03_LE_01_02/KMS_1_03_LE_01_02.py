class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def show_team(self):
        print(f"\nTeam: {self.name}\n")
        print("\nSpieler:\n")
        for player in self.players:
            print(f"{player.name}")

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                print(f"Spieler {name} wurde entfernt von: {self.name}")
                return
        print(f"Spieler {name} in {self.name} nicht gefunden")


def remove_team(teams, name):
    for team in teams:
        if team.name == name:
            teams.remove(team)
            print(f"Team {name} wurde entfernt!")
            return
    print(f"Team {name} nicht gefunden")


number_of_teams = int(input("Anzahl der Teams eingeben: "))
teams = []

for j in range(number_of_teams):
    team_name = input(f"Team Name von Team {j + 1} eingeben: ")
    players = []

    for i in range(11):
        player_name = input(f"Spieler Name {i + 1} von Team {j + 1}: ")
        players.append(Player(player_name))

    teams.append(Team(team_name, players))

while True:
    action = int(input("\n1 - Teams Anzeigen\n2 - Spieler entfernen\n3 - Team entfernen\n4 - beenden\n"))
    if action == 1:
        for team in teams:
            team.show_team()
    elif action == 2:
        team_name = input("Team Namen eingeben: ")
        player_name = input("Spieler Namen eingeben: ")
        for team in teams:
            if team.name == team_name:
                team.remove_player(player_name)
                break
        else:
            print(f"Team {team_name} nicht gefunden!")
    elif action == 3:
        team_name = input("Team Namen eingeben: ")
        remove_team(teams, team_name)
    elif action == 4:
        break
    else:
        print("Error")
