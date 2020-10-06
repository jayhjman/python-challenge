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
greatest_increase = {
    "index": 0,
    "value": 0
}
greatest_decrease = {
    "index": 0,
    "value": 0
}

# Open csv file for reading
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row first as there is a header in the file
    csv_header = next(csvreader)

    # Read each row of file
    for row in csvreader:
        profit = {
            "date": row[0],
            "profit": int(row[1])
        }
        bank_profits.append(profit)

# Sum the total amount of profit/losses
total_amount = 0

# Keep a rolling total of the average change month over month
average_total = 0

# Loop through bank profits calculating values (stopping 1 before the end)
for i in range(len(bank_profits)-1):

    total_amount += bank_profits[i]["profit"]
    profit_change = bank_profits[i+1]["profit"] - bank_profits[i]["profit"]
    average_total += profit_change

    if profit_change > greatest_increase["value"]:
        greatest_increase = {
            "value": profit_change,
            "index": i + 1
        }

    if profit_change < greatest_decrease["value"]:
        greatest_decrease = {
            "value": profit_change,
            "index": i + 1
        }

# We stopped on short in the loop above, make sure to add final value
total_amount += bank_profits[len(bank_profits)-1]["profit"]

# Change will be 1 less value than months since month to month comparision
average_change = average_total/(len(bank_profits)-1)

# Print out the summary table
print('Financial Analysis')
print('--------------------------------------------------------')
print(f'Total Months: {len(bank_profits)}')
print(f'Total: ${total_amount}')
print(f'Average  Change: ${round(average_change, 2)}')
print(
    f'Greatest Increase in Profits: {bank_profits[greatest_increase["index"]]["date"]} $({greatest_increase["value"]})')
print(
    f'Greatest Decrease in Profits: {bank_profits[greatest_decrease["index"]]["date"]} $({greatest_decrease["value"]})')
print('--------------------------------------------------------')
