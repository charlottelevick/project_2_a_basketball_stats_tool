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
teams_assignment = {team: [] for team in TEAMS}

# Loop over each team
for team in TEAMS:
    # Loop over each experienced player
    # and append the player to the current team being looped over
    for _ in range(exp_per_team):
        player = experienced_players.pop()
        teams_assignment[team].append(player)
# Loop over each team
for team in TEAMS:
    # Loop over each inexperienced player
    # and append the player to the current team being looped over
    for _ in range(inexp_per_team):
        player = inexperienced_players.pop()
        teams_assignment[team].append(player)
        
# Assign each team to its corresponding variable 
team1 = teams_assignment[TEAMS[0]]
team2 = teams_assignment[TEAMS[1]]
team3 = teams_assignment[TEAMS[2]]

# Function that returns a list of experienced players
def get_experienced_players(team):
    experienced_players = []
    for player in team:
        if player["experience"] == True:
            experienced_players.append(player)
    return experienced_players

# Get list of experienced players from each team and assign them to corresponding variables
team1_experienced_players = get_experienced_players(team1)
team2_experienced_players = get_experienced_players(team2)
team3_experienced_players = get_experienced_players(team3)

# Function that returns a list of inexperienced players
def get_inexperienced_players(team):
    inexperienced_players = []
    for player in team:
        if player["experience"] == False:
            inexperienced_players.append(player)
    return inexperienced_players

# Get list of inexperienced players from each team and assign them to corresponding variables
team1_inexperienced_players = get_inexperienced_players(team1)
team2_inexperienced_players = get_inexperienced_players(team2)
team3_inexperienced_players = get_inexperienced_players(team3)

# Calculate the average height of a team
def average_player_heights(team):
    player_heights = []
    for player in team:
        height = player["height"] 
        player_heights.append(height)  
    average_height = sum(player_heights) / len(player_heights)
    return average_height

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