# need to have "\AverageBird.csv" in current directory
import os
import csv

def main(bird_spec, weight):
    THRESHOLD = 0.6 #0.6 = 60% of expected weight
    bird_list = []
    weight_list = []
    avg_weight = 0
    dirpath = os.getcwd()
    f = dirpath + "\AverageBird.csv"
    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #reads the file to create 2 lists
        for row in csv_reader:
            bird_list.append(row[0])
            weight_list.append(row[1])
    
    if bird_spec in bird_list:
        avg_weight = weight_list[bird_list.index(bird_spec)]
    avg_weight = float(avg_weight)
    weight = float(weight)
    if (weight < avg_weight * THRESHOLD):
        return True
    return False

