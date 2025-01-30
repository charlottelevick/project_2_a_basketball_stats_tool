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

cleaned_data = clean_data(PLAYERS)

n = len(cleaned_data)
split_size = n // len(TEAMS)
team1 = cleaned_data[0:split_size]
team2 = cleaned_data[split_size:2*split_size]
team3 = cleaned_data[2*split_size:]

def get_experienced_players(team):
    experienced_players = []
    for player in team:
        if player["experience"] == True:
            experienced_players.append(player)
    return experienced_players
    
team1_experienced_players = get_experienced_players(team1)
team2_experienced_players = get_experienced_players(team2)
team3_experienced_players = get_experienced_players(team3)

def get_inexperienced_players(team):
    inexperienced_players = []
    for player in team:
        if player["experience"] == False:
            inexperienced_players.append(player)
    return inexperienced_players

team1_inexperienced_players = get_inexperienced_players(team1)
team2_inexperienced_players = get_inexperienced_players(team2)
team3_inexperienced_players = get_inexperienced_players(team3)

def average_player_heights(team):
    player_heights = []
    for player in team:
        height = player["height"] 
        player_heights.append(height)  
    average_height = sum(player_heights) / len(player_heights)
    return average_height

def players_on_teams(team):
    sorted_team_list = sorted(team, key=lambda d: d["height"])
    player_names = []
    for player in sorted_team_list:
        name = player["name"]
        player_names.append(name)
    joined_player_names = ", ".join(player_names)
    return joined_player_names

def guardians_on_teams(team):
    guardian_names = []
    for player in team:
        guardians = player["guardians"]
        for guardian in guardians:
            guardian_names.append(guardian)
    joined_guardian_names = ", ".join(guardian_names)
    return joined_guardian_names
    
def start_stats_tool():
    user_choice = input("BASKETBALL TEAM STATS TOOL\n\n----MENU----\n\nHere are your choices:\nA) Display Team Stats\nB) Quit\n")
    if user_choice.upper() == "A":
        user_option = input("\nEnter an option:\nA) Panthers\nB) Bandits\nC) Warriors\n")
        if user_option.upper() == "A":
            print(f"\nTeam: Panther's Stats\n--------------------\nTotal players: {len(team1)}\nTotal experienced: {len(team1_experienced_players)}\nTotal inexperienced: {len(team1_inexperienced_players)}\nAverage height: {round(average_player_heights(team1),1)}\nPlayers on Team: {players_on_teams(team1)}\nGuardians: {guardians_on_teams(team1)}")
            input("\nPress ENTER to continue...\n")
            start_stats_tool()
        elif user_option.upper() == "B":
            print(f"\nTeam: Bandit's Stats\n---------------------\nTotal players: {len(team2)}\nTotal experienced: {len(team2_experienced_players)}\nTotal inexperienced: {len(team2_inexperienced_players)}\nAverage height: {round(average_player_heights(team2),1)}\nPlayers on Team: {players_on_teams(team2)}\nGuardians: {guardians_on_teams(team2)}")
            input("\nPress ENTER to continue...\n")
            start_stats_tool()
        elif user_option.upper() == "C":
            print(f"\nTeam: Warrior's Stats\n--------------------\nTotal players: {len(team3)}\nTotal experienced: {len(team3_experienced_players)}\nTotal inexperienced: {len(team3_inexperienced_players)}\nAverage height: {round(average_player_heights(team3),1)}\nPlayers on Team: {players_on_teams(team3)}\nGuardians: {guardians_on_teams(team3)}")
            input("\nPress ENTER to continue...\n")
            start_stats_tool()
    elif user_choice.upper() == "B":
        sys.exit()
    else:
        print("Please try again")
        start_stats_tool()

start_stats_tool()