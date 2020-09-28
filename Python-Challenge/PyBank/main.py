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
    total_months = 0
    monthly_change = []
    date = []
    profit_loss = []
    total_profit = 0
    initial_profit = 0
    total_change_profits = 0

    # printing
    print("Financial Analysis")
    print("-------------------------------------------------------")

    # Total number of months included in dataset
    for row in csvreader:
        total_months = total_months + 1
        
        print("Total Months:" + str(total_months))  

# The net total amount of "Profit/Losses" over the entire period
        date.append(row[0])
        profit_loss.append(row[1])

        total_profit = total_profit + int(row[1])
        print("Total Profits:" + "$" + str(total_profit))
# The average of the changes in "profit/Losses" over the entire period
        average_profit = int(row[1])
        monthly_change_profits = average_profit - initial_profit
        monthly_change.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = average_profit
        average_change = (total_change_profits / total_months)
        print("Average Change:" + "$" + str(int(average_change)))

# The greatest increase in profits (date and amount) over the entire period
        greatest_decrease_profit = max(monthly_change)
        greatest_decrease_profit = min(monthly_change)  

# The greatest decrease in losses (date and amount) over hte entire period
        greatest_increase_dt = 
        greatest_decrease_dt = 