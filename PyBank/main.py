#
# PyBank
#
# Script that analyzes the financial records of the given bank.
# The purpose is show how many months the analysis covers, the
# total amount profit/losses, average change, greatest increase,
# and greatest decrease.
#

# Imports
import os
import csv


# Find the path of the current file
source_path = os.path.dirname(os.path.abspath(__file__))

# Create file path and name to read
file_path = os.path.join(source_path, 'Resources', 'budget_data.csv')

# List to hold the csv data in memory
bank_profits = []

# Average change
average_change = 0

# Greatest increase and decrease
greatest_increase = 0
greatest_decrease = 0

# Open csv file for reading
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row first as there is a header in the file
    csv_header = next(csvreader)

    # Read each row of file
    for row in csvreader:
        profit = {}
        profit["date"] = row[0]
        profit["profit"] = int(row[1])
        bank_profits.append(profit)

# Sum the total amount of profit/losses
total_amount = 0

# Loop through bank profits calculating values
for i in range(len(bank_profits)):
    total_amount += bank_profits[i]["profit"]


print('Financial Analysis')
print('--------------------------------------------------------')
print(f'Total Months: {len(bank_profits)}')
print(f'Total: ${total_amount}')
print(f'Average  Change: ${average_change}')
print(f'Greatest Increase in Profits: <Mth-Yr> $({greatest_increase})')
print(f'Greatest Decrease in Profits: <Mth-Yr> $({greatest_decrease})')
print('--------------------------------------------------------')
