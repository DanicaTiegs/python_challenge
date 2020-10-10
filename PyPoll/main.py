import os
import csv

csv_path = os.path.join("Resources","03-Python_HW_Instructions_PyPoll_Resources_election_data.csv")

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv.header = next(csvreader)