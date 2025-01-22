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
split_size = n // 3
team1 = PLAYERS[0:split_size]
team2 = PLAYERS[split_size:2*split_size]
team3 = PLAYERS[2*split_size:]
#print(f'Panthers: {team1}\n')
#print(f'Bandits : {team2}\n')
#print(f'Warriors : {team3}\n')

user_choice = input("BASKETBALL TEAM STATS TOOL\n\n----MENU----\n\nHere are your choices:\nA) Display Team Stats\nB) Quit\n")
if user_choice.upper() == "A":
    user_option = input("Enter an option:\nA) Panthers\nB) Bandits\nC) Warriors\n")
    if user_option.upper() == "A":
        print(f"Team: Panther's Stats\n--------------\nTotal players: {}\nTotal experienced: ?\nTotal inexperienced: \nAverage height: ?\nPlayers on Team: ?\nGuardians: ?\nPress ENTER to continue...")
elif user_choice.upper() == "B":
    sys.exit()
else:
    print("Please try again")
