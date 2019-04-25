import pandas as pd
import position_finder, k_nearest, fantasydata, normalize_NFL_combine
import csv
import requests
from data import code_dir
from flask import jsonify

print(code_dir)
# package like prime number example
# Use rest to fetch data

# Dataset urls, this will be online links
nfl_combine_data = 'https://drive.google.com/uc?export=download&id=1eSdscNIEaiyswQAq_acfbBLpUfiJRP4i'
nfl_2019_combine_data = "https://drive.google.com/uc?export=download&id=1g7CbEpdtWSQQGJGUWcwBieWkqPgBsmw2"
fantasy_data = "https://drive.google.com/uc?export=download&id=19rzVI1XLfHbPth7zN1T7BebwZsMp6AO_"

#code_dir = code_dir

def dd(url, filename):
    test = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(test.content)
    return


def download(output, url):
    output_file = code_dir + output
    dd(url=url, filename=output_file)
    return "data downloaded"

def ff_prediction(position):
    #position = 'WR'
    filename = '/nfl_2019_combine_data.csv'
    filename2 = '/nfl_combine_data.csv'
    filename3 = '/fantasy_data'

    download(filename, nfl_2019_combine_data)
    download(filename2, nfl_combine_data)
    download(filename3, fantasy_data)

    # Pandas read in, used in normalize_NFL_combine and k_nearest
    nfl_pd = pd.read_csv(code_dir + filename2)
    nfl_2019_pd = pd.read_csv(code_dir + filename)


    # Opens rookie combine data
    name_finder = open(code_dir + filename, 'r')
    print(name_finder)
    csv_pos_finder = csv.reader(name_finder)  # reads csv file
    print(csv_pos_finder)

    #
    # DONT CHANGE ANYTHING PAST HERE
    #

    # Empty Lists to Append to
    name_out = []
    points_out = []
    game_out = []

    # This will be inputted. Options: WR, RB, TE, QB, ALL
    position_compare = position
    # If we have an 'All" option in our Html, this will allow us to sort all positions
    position = position_compare

    # Adds Each Rookies Predicted Fantasy Values to Lists
    for row in csv_pos_finder:

        rookie_name = row[1]
        if(rookie_name != 'Player'):

            # Finds rookie position in combine dataset
            position = position_finder.position_finder(rookie_name, code_dir + filename)

            if(position == position_compare or position_compare == 'ALL'):

                # Normalizes our dataset, including only the specific position entered
                nfl_normalized, nfl_normalized_2019 = normalize_NFL_combine.normalize_nfl_combine(nfl_pd, nfl_2019_pd, position)

                # Finds three nearest neighbors
                lst = k_nearest.k_nearest(nfl_normalized, nfl_normalized_2019, nfl_2019_pd, nfl_pd, rookie_name)

                # Finds three neighbors in fantasy_data_set and averages their points over the seasons
                points, game = fantasydata.fantasydata(code_dir + filename3, lst)
                name_out.append(rookie_name)
                points_out.append(points)
                game_out.append(game)

    # Creates Panda Dataframe
    df = pd.DataFrame({"Name": name_out, "Season Points": points_out, "Avg Points/Game": game_out})
    df = df.sort_values(by=['Season Points'], ascending=False)
    df = df.reset_index(drop=True)
    df.to_csv('Player_Rank.csv')

    return(df.to_html())
    
