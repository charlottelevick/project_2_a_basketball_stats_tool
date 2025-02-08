from constants import TEAMS, PLAYERS

# Function that cleans data imported from PLAYERS
# and changes it to desired data structure
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

# Called clean_data function with the argument PLAYERS constant
# and assign the return value to cleaned_data variable
cleaned_data = clean_data(PLAYERS)

# Loop over cleaned_data and check if each player's experience is True
experienced_players = [player for player in cleaned_data if player["experience"]]
# Loop over cleaned_data and check if each player's experience is NOT True
inexperienced_players = [player for player in cleaned_data if not player["experience"]]

# Length of Teams constant to figure out how many teams there needs to be
num_teams = len(TEAMS)

# Figure out number of experienced players per team
# by dividing the number of teams by the number of experienced players
exp_per_team = len(experienced_players) // num_teams
# Figure out number of inexperienced players per team
# by dividing the number of teams by the number of inexperienced players
inexp_per_team = len(inexperienced_players) // num_teams

# Create a dictionary which has a key for each team
# and each value is an empty list
teams_assignment = {team: {"players": [], "experience": 0, "inexperience": 0, "avg_height": 0} for team in TEAMS}

print(teams_assignment)

# Calculate the average height of a team
def average_player_heights(team):
    player_heights = []
    for player in team:
        height = player["height"] 
        player_heights.append(height)  
    average_height = sum(player_heights) / len(player_heights)
    return round(average_height,1)

# Loop over each team
for team in TEAMS:
    # Loop over each experienced player
    # and append the player to the current team being looped over
    for _ in range(exp_per_team):
        player = experienced_players.pop()
        teams_assignment[team]["players"].append(player)
        teams_assignment[team]["experience"] += 1
        
# Loop over each team
for team in TEAMS:
    # Loop over each inexperienced player
    # and append the player to the current team being looped over
    for _ in range(inexp_per_team):
        player = inexperienced_players.pop()
        teams_assignment[team]["players"].append(player)
        teams_assignment[team]["inexperience"] += 1
        
    # Calculate average height of current team being looped
    teams_assignment[team]["avg_height"] = average_player_heights(teams_assignment[team]["players"])
        
# Assign each team to its corresponding variable 
team1 = teams_assignment[TEAMS[0]]
team2 = teams_assignment[TEAMS[1]]
team3 = teams_assignment[TEAMS[2]]

# Return list of players ordered by height
def players_on_teams(team):
    sorted_team_list = sorted(team, key=lambda d: d["height"])
    player_names = []
    for player in sorted_team_list:
        name = player["name"]
        player_names.append(name)
    joined_player_names = ", ".join(player_names)
    return joined_player_names

# Return a list of guardians for a team
def guardians_on_teams(team):
    guardian_names = []
    for player in team:
        guardians = player["guardians"]
        for guardian in guardians:
            guardian_names.append(guardian)
    joined_guardian_names = ", ".join(guardian_names)
    return joined_guardian_names
    
# Function that allows interaction and input from the user
def start_stats_tool():
    user_choice = input("BASKETBALL TEAM STATS TOOL\n\n----MENU----\n\nHere are your choices:\nA) Display Team Stats\nB) Quit\n")
    if user_choice.upper() == "A":
        user_option = input("\nEnter an option:\nA) Panthers\nB) Bandits\nC) Warriors\n")
        if user_option.upper() == "A":
            print(f"\nTeam: Panther's Stats\n--------------------\nTotal players: {len(team1["players"])}\nTotal experienced: {team1["experience"]}\nTotal inexperienced: {team1["inexperience"]}\nAverage height: {team1["avg_height"]}\nPlayers on Team: {players_on_teams(team1["players"])}\nGuardians: {guardians_on_teams(team1["players"])}")
            input("\nPress ENTER to continue...\n")
            start_stats_tool()
        elif user_option.upper() == "B":
            print(f"\nTeam: Bandit's Stats\n---------------------\nTotal players: {len(team2["players"])}\nTotal experienced: {team2["experience"]}\nTotal inexperienced: {team2["inexperience"]}\nAverage height: {team2["avg_height"]}\nPlayers on Team: {players_on_teams(team2["players"])}\nGuardians: {guardians_on_teams(team2["players"])}")
            input("\nPress ENTER to continue...\n")
            start_stats_tool()
        elif user_option.upper() == "C":
            print(f"\nTeam: Warrior's Stats\n--------------------\nTotal players: {len(team3["players"])}\nTotal experienced: {team3["experience"]}\nTotal inexperienced: {team3["inexperience"]}\nAverage height: {team3["avg_height"]}\nPlayers on Team: {players_on_teams(team3["players"])}\nGuardians: {guardians_on_teams(team3["players"])}")
            input("\nPress ENTER to continue...\n")
            start_stats_tool()
        else:
            print("Please try again")
            start_stats_tool()
    elif user_choice.upper() == "B":
        exit()
    else:
        print("Please try again")
        start_stats_tool()

# This function will run only if the app.py file is run in the python command line
# i.e. python app.py
if __name__ == "__main__": 
    start_stats_tool()