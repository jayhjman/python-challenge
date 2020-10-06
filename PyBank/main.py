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


#
# read_profits_from_csv
#
# Read the file from the csv file and populate the profit list then
# return the profit list back to the caller

def read_profits_from_csv(input_file):

    profits = []

    # Open csv file for reading
    with open(input_file) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip header row first as there is a header in the file
        csv_header = next(csvreader)

        # Read each row of file append to our list to be processed later
        for row in csvreader:
            profit = {
                "date": row[0],
                "profit": int(row[1])
            }
            profits.append(profit)

        return profits


#
# output_results
#
# Output to console and file the string passed in

def output_results(output_file, string_to_output):

    # Print out the summary table
    print(string_to_output)

    # Write the output results text file
    results_file = open(output_file, 'w')
    num_of_chars = results_file.write(string_to_output)
    results_file.close()


#
# main
#
# main function for executing the program

def main():

    # Find the path of the current file
    source_path = os.path.dirname(os.path.abspath(__file__))

    # Create read/write file paths with file names
    read_file = os.path.join(source_path, 'Resources', 'budget_data.csv')
    write_file = os.path.join(source_path, 'analysis', 'results.txt')

    # List to hold the csv data in memory
    bank_profits = read_profits_from_csv(read_file)

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

    # Sum the total amount of profit/losses
    total_amount = 0

    # Keep a rolling total of the average change month over month
    average_total = 0

    # Loop through bank profits calculating values (stopping 1 before the end to avoid index out of range issues)
    for i in range(len(bank_profits)-1):

        # Count up totals for later calculations
        total_amount += bank_profits[i]["profit"]
        profit_change = bank_profits[i+1]["profit"] - bank_profits[i]["profit"]
        average_total += profit_change

        # Track the greatest increase between months
        if profit_change > greatest_increase["value"]:
            greatest_increase = {
                "value": profit_change,
                "index": i + 1
            }

        # Track the greatest decrease between months
        if profit_change < greatest_decrease["value"]:
            greatest_decrease = {
                "value": profit_change,
                "index": i + 1
            }

    # We stopped on short in the loop above, make sure to add final value
    total_amount += bank_profits[len(bank_profits)-1]["profit"]

    # Change will be 1 less value than months since month to month comparision
    average_change = average_total/(len(bank_profits)-1)

    # Create the output string
    output_string = 'Financial Analysis\n'
    output_string += '--------------------------------------------------------\n'
    output_string += str.format(f'Total Months: {len(bank_profits)}\n')
    output_string += str.format(f'Total: ${total_amount}\n')
    output_string += str.format(
        f'Average  Change: ${round(average_change, 2)}\n')
    output_string += str.format(
        f'Greatest Increase in Profits: {bank_profits[greatest_increase["index"]]["date"]} $({greatest_increase["value"]})\n')
    output_string += str.format(
        f'Greatest Decrease in Profits: {bank_profits[greatest_decrease["index"]]["date"]} $({greatest_decrease["value"]})\n')
    output_string += '--------------------------------------------------------'

    output_results(write_file, output_string)


if __name__ == "__main__":
    main()
