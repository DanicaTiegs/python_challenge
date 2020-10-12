import os
import csv

csv_path = os.path.join("Resources","03-Python_HW_Instructions_PyPoll_Resources_election_data.csv")

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv.header = next(csvreader)

#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.