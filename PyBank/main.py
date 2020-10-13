import os
import csv

csv_path = os.path.join("Resources","03-Python_HW_Instructions_PyBank_Resources_budget_data.csv")

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv.header = next(csvreader)
    #for row in csvfile:
        #print (row)

    month_count=0
    month_total = 0 
    previous = 0
    total_change = 0
    greatest_profit = 0 
    greatest_loss = 99999999999 
    greatest_month = ""
    lowest_month = ""
    

    for row in csvreader:
        #pybank_data[row[0]] = months
        month_count = month_count + 1 
        month_total = month_total + int(row[1])
        current = int(row[1])
        change = current - previous
        if month_count > 1:
            total_change = total_change + change
            if change > greatest_profit:
                greatest_profit = change
                greatest_month = row[0]
            if change < greatest_loss:
                greatest_loss = change
                lowest_month = row[0]
        previous = int(row[1])
    print("financial analysis")
    print("--------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: {month_total}")
    print(f"Average Change: ${total_change/(month_count - 1)}")
    print(f"Greatest Increase Profits: {greatest_month} (${greatest_profit})")
    print(f"Greatest Decrease: {lowest_month} (${greatest_loss})")



