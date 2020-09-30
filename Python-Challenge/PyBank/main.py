import os
import csv 

# path to collect data 
pybank_csv = os.path.join('..', 'csv_files', 'budget_data.csv')

#declaring all my variables

total_months = []
monthly_change = []
net_total = []
profit_loss = []


#reading the file
with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

#remove header from count
    
    csv_header = next(csvreader)

# printing
    print("Financial Analysis")
    print("-------------------------------------------------------")

# Total number of months included in dataset
    for row in csv.reader(csvfile):
        total_months.append(row[0])       

# The net total amount of "Profit/Losses" over the entire period
        net_total.append(int(row[1]))
       

# The average of the changes in "profit/Losses" over the entire period
    for i in range(len(net_total)-1):
            profit_loss.append(net_total[i + 1] - net_total[i])
            print(f'{len(total_months)}')
            print(f'{sum(net_total)}')    

# The greatest increase in profits (date and amount) over the entire period
greatest_increase_profit = max(monthly_change)
greatest_decrease_profit = min(monthly_change)
monthly_increase = monthly_change.index(max(monthly_change)) + 1
Monthly_decrease = monthly_change.index(min(monthly_change)) + 1
print(f'{round(sum(monthly_change)/len(monthly_change),2)}')

        

# The greatest decrease in losses (date and amount) over hte entire period
greatest_increase_dt = total_months[monthly_change.index(greatest_increase_profit)]
greatest_decrease_dt = total_months[monthly_change.index(greatest_decrease_profit)]
print(f'{total_months[monthly_increase]} (${(str(greatest_increase_profit))}')