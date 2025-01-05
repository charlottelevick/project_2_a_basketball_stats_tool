from constants import TEAMS
from constants import PLAYERS

def clean_data(data):
    cleaned = []
    for player in data:
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
    
print(clean_data(PLAYERS))