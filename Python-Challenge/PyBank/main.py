import os
import csv 

# path to collect data 
pybank_csv = os.path.join('..', 'csv_files', 'budget_data.csv')
print(pybank_csv) 

#reading the file
with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# printing
print("Financial Analysis")
print("-------------------------------------------------------")

# Total number of months included in dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over hte entire period