import os
import csv 

# path to collect data 
pybank_csv = os.path.join('..', 'csv_files', 'budget_data.csv')

#reading the file
with open(pybank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #declaring all my variables
    total_months = []
    profit_loss = []
    average_change = []
    greatest_increase_dt = "" 
    greatest_decrease_dt = ""

# printing
print("Financial Analysis")
print("-------------------------------------------------------")

# Total number of months included in dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over hte entire period