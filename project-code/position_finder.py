# Gets rookie position, i dont know how to do this in pandas so I reopened in my way. Feel free to
# change so it uses pandas if u know how
import csv


def position_finder(rookie_name, rookiedata):
    pos_finder = open(rookiedata)
    csv_pos_finder = csv.reader(pos_finder) # reads csv file
    position = 0

    for row in csv_pos_finder:
        if(row[1] == rookie_name):
            position = row[2]
    return position
