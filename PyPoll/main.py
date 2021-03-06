import os
import csv

csv_path = os.path.join("Resources","03-Python_HW_Instructions_PyPoll_Resources_election_data.csv")

candidates = {}
total_votes = 0 

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv.header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] = candidates[row[2]] + 1
print("election results")
print("--------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")
winner = ""
winner_votes = 0 
for candidate in candidates:
    print(f"{candidate} {(candidates[candidate]/total_votes) * 100:.2f}% {candidates[candidate]} ")
    if candidates[candidate] > winner_votes:
        winner_votes = candidates[candidate]
        winner = candidate
print("--------------------")        
print(f"Winner: {winner}")
print("--------------------") 

#how to define outpath?

output_path = os.path.join("Analysis", "Analysis.txt")
with open(output_path, "w") as textfile:
    textfile.write("election results")
    textfile.write("\n")
    textfile.write("--------------------")
    textfile.write("\n")
    textfile.write(f"Total Votes: {total_votes}")
    textfile.write("\n")
    textfile.write("--------------------")
    textfile.write("\n")
    # How do I have an iteration print out correctly in textfile?
    textfile.write(f"{candidate} {(candidates[candidate]/total_votes) * 100:.2f}% {candidates[candidate]} ")
    textfile.write("\n")
    textfile.write(f"Winner: {winner}")
   