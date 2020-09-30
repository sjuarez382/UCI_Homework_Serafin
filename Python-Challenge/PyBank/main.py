import os
import csv 

# path to collect data 
pybank_csv = os.path.join('..', 'csv_files', 'budget_data.csv')

#reading the file
with open(pybank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

#remove header from count
    
    csv_header = next(csvreader)

#declaring all my variables

    monthly_change = []
    total_months = []
    net_total = []
    profit_loss = []

# printing
    print("Financial Analysis")
    print("-------------------------------------------------------")

# Total number of months included in dataset
    for row in csv.reader(csvfile):
        total_months.append(row[0])       

# The net total amount of "Profit/Losses" over the entire period
        net_total.append(int(row[1]))
       

# The average of the changes in "profit/Losses" over the entire period
       

# The greatest increase in profits (date and amount) over the entire period
        #greatest_increase_profit = max(monthly_change)
        #greatest_decrease_profit = min(monthly_change)  

# The greatest decrease in losses (date and amount) over hte entire period
        #greatest_increase_dt = date[monthly_change.index(greatest_increase_profit)]
        #greatest_decrease_dt = date[monthly_change.index(greatest_decrease_profit)]