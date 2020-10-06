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

# Count the number of months in the file
number_of_months = 0

# Sum the total amount of profit/losses
total_amount = 0

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
        number_of_months += 1
        total_amount += int(row[1])


print('Financial Analysis')
print('--------------------------------------------------------')
print(f'Total Months: {number_of_months}')
print(f'Total: ${total_amount}')
print(f'Average  Change: ${average_change}')
print(f'Greatest Increase in Profits: <Mth-Yr> $({greatest_increase})')
print(f'Greatest Decrease in Profits: <Mth-Yr> g$({greatest_decrease})')
print('--------------------------------------------------------')
