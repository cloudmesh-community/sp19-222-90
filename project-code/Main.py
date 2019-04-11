import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance
import position_finder, k_nearest, fantasydata, normalize_NFL_combine

nfl = pd.read_csv("/home/gotts/Desktop/E222/Project/combine_data.csv")
nfl_2019 = pd.read_csv("/home/gotts/Desktop/E222/Project/2019_combine_data.csv")
rookie_name = "Hakeem Butler"

# Call rookie function, pass in rookie combine dataset
position = position_finder.position_finder(rookie_name, "/home/gotts/Desktop/E222/Project/2019_combine_data.csv")

nfl_normalized, nfl_normalized_2019 = normalize_NFL_combine.normalize_nfl_combine(nfl,nfl_2019, position)

lst = k_nearest.k_nearest(nfl_normalized, nfl_normalized_2019, nfl_2019, nfl, rookie_name)

points, game = fantasydata.fantasydata("/home/gotts/Desktop/E222/Project/ffdata.csv", lst)
print("Season Points %d" % points)
print("Points Per Game %d" % game)
