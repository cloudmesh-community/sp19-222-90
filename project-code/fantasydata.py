import csv


def fantasydata(ffdatain, lst):
    ffdata = open(ffdatain)
    csv_ffdata = csv.reader(ffdata)  # reads csv file
    points = 0
    seasons = 0
    avg_points_year = 0
    avg_points_game = 0

    # accounts for '*' and '*+' in FF dataset
    lst2 = []
    lst3 = []
    for i in range(3):
        lstt2 = lst[i] + '*'
        lstt3 = lst[i] + '*' + '+'
        lst2.append(lstt2)
        lst3.append(lstt3)

    # loop over name matches and add up points and seasons for 3 players
    for row in csv_ffdata:
        # no * or +
        if ((lst[0] == row[0]) or (lst[1] == row[0]) or (lst[2] == row[0])):
            string = row[3]  # all data is in string format
            if(row[3] != ''):
                points += int(string)  # convert to int and add for total points
                seasons += 1;

        # just *
        if ((lst2[0] == row[0]) or (lst2[1] == row[0]) or (lst2[2] == row[0])):
            string = row[3]  # all data is in string format
            points += int(string)  # convert to int and add for total points
            seasons += 1;

        # just *+
        if ((lst3[0] == row[0]) or (lst3[1] == row[0]) or (lst3[2] == row[0])):
            string = row[3]  # all data is in string format
            points += int(string)  # convert to int and add for total points
            seasons += 1;

    # average points
    if (points != 0):
        avg_points_year = points / seasons
        avg_points_game = avg_points_year / 16

    ffdata.close()

    return avg_points_year, avg_points_game
