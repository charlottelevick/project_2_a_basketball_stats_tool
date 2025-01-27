from constants import TEAMS, PLAYERS
import sys

def clean_data(player_list):
    cleaned = []
    for player in player_list:
        fixed = {}
        fixed["name"] = player["name"]
        guardians_list = []
        if "and" in player["guardians"]:
            guardians_list = player["guardians"].split(" and ")
        else:
            guardians_list.append(player["guardians"]) 
        fixed["guardians"] = guardians_list
        split_height_as_str = player["height"].split(" ")[0]
        fixed["height"] = int(split_height_as_str)
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        cleaned.append(fixed)
    return cleaned

n = len(PLAYERS)
split_size = n // len(TEAMS)
team1 = PLAYERS[0:split_size]
team2 = PLAYERS[split_size:2*split_size]
team3 = PLAYERS[2*split_size:]

def start_game():
    user_choice = input("BASKETBALL TEAM STATS TOOL\n\n----MENU----\n\nHere are your choices:\nA) Display Team Stats\nB) Quit\n")
    if user_choice.upper() == "A":
        user_option = input("\nEnter an option:\nA) Panthers\nB) Bandits\nC) Warriors\n")
        if user_option.upper() == "A":
            print(f"\nTeam: Panther's Stats\n--------------\nTotal players: {len(team1)}\nTotal experienced: ?\nTotal inexperienced: \nAverage height: ?\nPlayers on Team: ?\nGuardians: ?")
            input("\nPress ENTER to continue...\n")
            start_game()
        elif user_option.upper() == "B":
            print(f"\nTeam: Bandit's Stats\n--------------\nTotal players: {len(team2)}\nTotal experienced: ?\nTotal inexperienced: \nAverage height: ?\nPlayers on Team: ?\nGuardians: ?")
            input("\nPress ENTER to continue...\n")
            start_game()
        elif user_option.upper() == "C":
            print(f"\nTeam: Warrior's Stats\n--------------\nTotal players: {len(team3)}\nTotal experienced: ?\nTotal inexperienced: \nAverage height: ?\nPlayers on Team: ?\nGuardians: ?")
            input("\nPress ENTER to continue...\n")
            start_game()
    elif user_choice.upper() == "B":
        sys.exit()
    else:
        print("Please try again")

start_game()