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
# process_profits_from_csv
#
# Read the rows from the csv file and as you go through them to calculate:
#
#    1. Total months being processed
#    2. Total amount profit over all the months processed
#    3. Average change in profit month over month
#    4. Greatest increase in profit from month to month
#    5. Greatest decrease in profit from month to month
#
# Algorithm processes by keeping previous months data and doing calculations
# using the current month.
#

def process_profits_from_csv(input_file):

    # Zero out totals for calculations
    total_months = 0
    total_amount = 0

    # Total of profit change month over month, used later to calculate average
    total_profit_change = 0

    # Placeholder for the greatest profit increase
    greatest_increase = {
        "date": "",
        "value": 0
    }

    # Placeholder for greatest profit decrease
    greatest_decrease = {
        "date": "",
        "value": 0
    }

    # Open csv file for reading
    with open(input_file) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip header row first as there is a header in the file
        csv_header = next(csvreader)

        # Create an empty previous row to start
        previous_row = {}

        # Read each row of file append to our list to be processed later
        for row in csvreader:

            # Get total number of months and profit amounts
            total_months += 1
            total_amount += int(row[1])

            # Start doing the calculations after previous row is set (skips first row)
            if bool(previous_row):

                # profit change need for greatest calculation and total profits needed for average
                profit_change = int(row[1]) - previous_row["value"]
                total_profit_change += profit_change

                # Track the greatest increase between months
                if profit_change > greatest_increase["value"]:
                    greatest_increase = {
                        "date": row[0],
                        "value": profit_change
                    }

                # Track the greatest decrease between months
                if profit_change < greatest_decrease["value"]:
                    greatest_decrease = {
                        "date": row[0],
                        "value": profit_change
                    }

            # Track previous row for month to month calculations
            previous_row = {
                "date": row[0],
                "value": int(row[1])
            }

    # Build a summary dict for display purposes to return to caller
    return {
        "total_months": total_months,
        "total_amount": total_amount,
        "average_change": (total_profit_change/(total_months - 1)),
        "greatest_increase_month": greatest_increase["date"],
        "greatest_increase_value": greatest_increase["value"],
        "greatest_decrease_month": greatest_decrease["date"],
        "greatest_decrease_value": greatest_decrease["value"],
    }


#
# output_results
#
# Output to console and file the string passed in


def output_results(output_file, bank_info):

    # Create the output string
    output_string = 'Financial Analysis\n'
    output_string += '--------------------------------------------------------\n'
    output_string += str.format(f'Total Months: {bank_info["total_months"]}\n')
    output_string += str.format(f'Total: ${bank_info["total_amount"]}\n')
    output_string += str.format(
        f'Average  Change: ${round(bank_info["average_change"], 2)}\n')
    output_string += str.format(
        f'Greatest Increase in Profits: {bank_info["greatest_increase_month"]} $({bank_info["greatest_increase_value"]})\n')
    output_string += str.format(
        f'Greatest Decrease in Profits: {bank_info["greatest_decrease_month"]} $({bank_info["greatest_decrease_value"]})\n')
    output_string += '--------------------------------------------------------'

    # Print out the summary table
    print(output_string)

    # Write the output results text file
    results_file = open(output_file, 'w')
    num_of_chars = results_file.write(output_string)
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

    # Read and process data from the cvs file, could be rather large so process as you read
    bank_info = process_profits_from_csv(read_file)

    # Output to both console and file
    output_results(write_file, bank_info)


# Call the main function
if __name__ == "__main__":
    main()
