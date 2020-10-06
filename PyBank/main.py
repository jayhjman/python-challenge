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

print(f'file_path: {file_path}')

with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
