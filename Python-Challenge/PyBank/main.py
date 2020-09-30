import os
import csv 

# path to collect data 
pybank_csv = os.path.join('..', 'csv_files', 'budget_data.csv')

#declaring all my variables

total_months = []
monthly_change = []
net_total = []


#reading the file
with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

#remove header from count
    
    csv_header = next(csvreader)



# Total number of months included in dataset
    for row in csv.reader(csvfile):
        total_months.append(row[0])       

# The net total amount of "Profit/Losses" over the entire period
        net_total.append(int(row[1]))


# The average of the changes in "profit/Losses" over the entire period
    for i in range(len(net_total)-1):
            monthly_change.append(net_total[i + 1] - net_total[i])
              

# The greatest increase in profits (date and amount) over the entire period
greatest_increase_profit = max(monthly_change)
greatest_decrease_profit = min(monthly_change)
monthly_increase = monthly_change.index(max(monthly_change)) + 1
Monthly_decrease = monthly_change.index(min(monthly_change)) + 1
        

# The greatest decrease in losses (date and amount) over hte entire period
greatest_increase_dt = total_months[monthly_change.index(greatest_increase_profit)]
greatest_decrease_dt = total_months[monthly_change.index(greatest_decrease_profit)]



# printing
print("Financial Analysis")
print("-------------------------------------------------------")
print(f'Total Months: {len(total_months)}')
print(f'Total: ${sum(net_total)}')
print(f'Average Change:{round(sum(monthly_change)/len(monthly_change),2)}')
print(f'Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(greatest_increase_profit))})')
print(f'Greatest Decrease in Profits: {total_months[Monthly_decrease]} (${(str(greatest_decrease_profit))})')

 #Final script, print to terminal and exporting to text file
csvfile = os.path.join('Analysis', "Financial_Analys_Summary_PyBank.txt")
with open(csvfile, 'w') as file:

# Writting to text file
        file.write("Financial Analysis")
        file.write("\n")
        file.write("-------------------------------------------------------")
        file.write("\n")
        file.write(f'Total Months: {len(total_months)}')
        file.write("\n")
        file.write(f'Total: ${sum(net_total)}')
        file.write("\n")
        file.write(f'Average Change:{round(sum(monthly_change)/len(monthly_change),2)}')
        file.write("\n")
        file.write(f'Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(greatest_increase_profit))})')
        file.write("\n")
        file.write(f'Greatest Decrease in Profits: {total_months[Monthly_decrease]} (${(str(greatest_decrease_profit))})')
        
