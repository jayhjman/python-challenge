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


# Find the path of the current file
source_path = os.path.dirname(os.path.abspath(__file__))

# Create file path and name to read
file_path = os.path.join(source_path, 'Resources', 'budget_data.csv')

print(f'file_path: {file_path}')
