from constants import TEAMS
from constants import PLAYERS

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

def balance_teams(player_list, teams):
    NUM_PLAYERS_TEAM = len(player_list) / len(teams)
    print(int(NUM_PLAYERS_TEAM))
    
balance_teams(PLAYERS, TEAMS)
    
print(clean_data(PLAYERS))