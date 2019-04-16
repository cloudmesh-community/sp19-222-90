import pandas as pd
import position_finder, k_nearest, fantasydata, normalize_NFL_combine
import csv
#import requests

# Dataset urls, this will be online links
nfl_combine_data = "/home/gotts/Desktop/E222/Project/combine_data.csv"
#nfl_combine_data = requests.get('https://docs.google.com/spreadsheets/d/1JWyqpXNCblMogJ0CydsgleBUPaZ1V1zc1t01FmMO3P8/edit?usp=sharing')

nfl_2019_combine_data = "/home/gotts/Desktop/E222/Project/2019_combine_data.csv"
#nfl_2019_combine_data = requests.get('https://docs.google.com/spreadsheets/d/1JWyqpXNCblMogJ0CydsgleBUPaZ1V1zc1t01FmMO3P8/edit?usp=sharing')

fantasy_data = "/home/gotts/Desktop/E222/Project/ffdata.csv"
#fantasy_data = requests.get('https://docs.google.com/spreadsheets/d/1JWyqpXNCblMogJ0CydsgleBUPaZ1V1zc1t01FmMO3P8/edit?usp=sharing')

# Pandas read in, used in normalize_NFL_combine and k_nearest
nfl_pd = pd.read_csv(nfl_combine_data)
nfl_2019_pd = pd.read_csv(nfl_2019_combine_data)

# Opens rookie combine data
name_finder = open(nfl_2019_combine_data)
csv_pos_finder = csv.reader(name_finder)  # reads csv file

# Empty Lists to Append to
name_out = []
points_out= []
game_out = []

# This will be inputted. Options: WR, RB, TE, QB, ALL
position_compare = 'WR'
# If we have an 'All" option in our Html, this will allow us to sort all positions
position = position_compare

# Adds Each Rookies Predicted Fantasy Values to Lists
for row in csv_pos_finder:

    rookie_name = row[1]
    if(rookie_name != 'Player'):

        # Finds rookie position in combine dataset
        position = position_finder.position_finder(rookie_name, nfl_2019_combine_data)

        if(position == position_compare or position_compare == 'All'):

            # Normalizes our dataset, including only the specific position entered
            nfl_normalized, nfl_normalized_2019 = normalize_NFL_combine.normalize_nfl_combine(nfl_pd, nfl_2019_pd, position)

            # Finds three nearest neighbors
            lst = k_nearest.k_nearest(nfl_normalized, nfl_normalized_2019, nfl_2019_pd, nfl_pd, rookie_name)

            # Finds three neighbors in fantasy_data_set and averages their points over the seasons
            points, game = fantasydata.fantasydata(fantasy_data, lst)
            name_out.append(rookie_name)
            points_out.append(points)
            game_out.append(game)

# Creates Panda Dataframe
df = pd.DataFrame({"Name": name_out, "Season Points": points_out, "Avg Points/Game": game_out})
df = df.sort_values(by=['Season Points'], ascending=False)
df = df.reset_index(drop=True)
df.to_excel('Player_Rank.xlsx')
print(df)
