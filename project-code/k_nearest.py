import pandas as pd
from scipy.spatial import distance


def k_nearest(nfl_normalized, nfl_normalized_2019, nfl_2019, nfl, rookie_name):
    # Select 2019 player in normalized dataset
    selected_normalized = nfl_normalized_2019[nfl_2019["Player"] == rookie_name]

    # Calculate Euclidean Distance, of every player in dataset
    euclidean_distances = nfl_normalized.apply(lambda row: distance.euclidean(row, selected_normalized), axis=1)

    distance_frame = pd.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
    distance_frame.sort_values("dist", inplace=True)
    # print(distance_frame)

    # Calculates three closest
    three_closest = [distance_frame.iloc[0]["idx"], distance_frame.iloc[1]["idx"], distance_frame.iloc[2]["idx"]]
    lst = []  # stores three closest players

    for i in range(3):
        lstt = (nfl.iloc[int(three_closest[i])]["Player"])
        lst.append(lstt)

    return lst
