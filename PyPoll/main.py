#
# PyPoll
#
# Script that analyzes the election records for the given candidates.
# The purpose is show who won the election, the percentage and total
# breakdown of votes for each candidate, and final overall total vote
# count.

# Imports
import os
import csv

#
# process_votes_from_csv
#
# Read the rows from the csv file and process the voter candidate information
#
# Process the data and produce a summary dictionary to include the following:
#
#    1. Total number of votes
#    2. Total amount of votes for each candidate
#    3. The percentage of votes each candidate received
#    4. Determine the winner with the highest number of votes


def process_votes_from_csv(input_file):

    # Dictionary to hold candidate information
    candidate_info = {}

    # Overall number of votes
    total_overall_votes = 0

    # Dictionary for winner information
    winner = {
        "candidate": "",
        "votes": 0,
    }

    # Open csv file for reading
    with open(input_file) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip header row first as there is a header in the file
        csv_header = next(csvreader)

        # Dictionary to hold candidates
        candidates = {}

        # Read each row and do the counts of votes overall and for each candidate
        for row in csvreader:
            total_overall_votes += 1
            if row[2] in candidates:
                candidates[row[2]] += 1
            else:
                candidates[row[2]] = 1

        # Loop to calculate the winner and calculate the %
        for candidate in candidates:

            # calculate the percentage of votes to be added to the summary later
            candidate_info[candidate] = {
                "votes": candidates[candidate],
                "percent_votes": (candidates[candidate] / total_overall_votes) * 100
            }

            # If this candidate's votes are higher than the last highest then they win
            if candidates[candidate] > winner["votes"]:
                winner["candidate"] = candidate
                winner["votes"] = candidates[candidate]

    # Return the summary table
    return {
        "total_votes": total_overall_votes,
        "candidates": candidate_info,
        "winner": winner["candidate"],
    }


#
# output_results
#
# Output to console and file the summary passed by formatting it to text

def output_results(output_file, summary):

    # Format the string for the election results
    string_to_output = 'Election Results\n'
    string_to_output += '-------------------------------\n'
    string_to_output += str.format(f'Total Votes: {summary["total_votes"]}\n')
    string_to_output += '-------------------------------\n'

    # Loop through candidates to get detailed info on them
    candidates = summary["candidates"]
    for candidate in candidates:
        candidate_info = candidates[candidate]
        string_to_output += str.format(
            f'{candidate}: {candidate_info["percent_votes"]:.3f}% ({candidate_info["votes"]})\n')

    # Winner, Winner, Chicken Dinner
    string_to_output += '-------------------------------\n'
    string_to_output += str.format(f'Winner: {summary["winner"]}\n')
    string_to_output += '-------------------------------'

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
    read_file = os.path.join(source_path, 'Resources', 'election_data.csv')
    write_file = os.path.join(source_path, 'analysis', 'results.txt')

    # Get the summary breakdown of votes, %, totals, and winner
    summary_of_votes = process_votes_from_csv(read_file)

    # Print the summary results to the console and files
    output_results(write_file, summary_of_votes)


# Call the main function
if __name__ == "__main__":
    main()
