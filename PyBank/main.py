import os
import csv

csv_path = os.path.join("Resources","03-Python_HW_Instructions_PyBank_Resources_budget_data.csv")

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv.header = next(csvreader)
    #for row in csvfile:
        #print (row)

#The total number of months included in the dataset

data=list(csvreader)
    row_count = len(data)

month_total = []
for row in csvreader:
    values = row[1]
    month_total.append(values)
print (month_total)

#The net total amount of "Profit/Losses" over the entire period

profits_losses = []
for row in csvreader:
    for column in row:
        values = row[1]
        profits_losses.append(values)
print(profits_losses)

#The average of the changes in "Profit/Losses" over the entire period

profits_losses = []
for row in csvreader:
    for column in row:
        values = row[1]
        profits_losses.append(values)
print(profits_losses)


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period
