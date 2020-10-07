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
# read_voters_from_csv
#
# Read the file from the csv file and populate the voters list then
# return the voters list back to the caller


def read_voters_from_csv(input_file):

    voters = []

    # Open csv file for reading
    with open(input_file) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip header row first as there is a header in the file
        csv_header = next(csvreader)

        # Read each row of file append to our list to be processed later
        for row in csvreader:
            voter = {
                "voter_id": row[0],
                "county": row[1],
                "candidate": row[2]
            }
            voters.append(voter)

    return voters

#
# process_voters
#
# Take the election voter list and find
#    1. Total number of votes
#    2. Total amount of votes for each candidate
#    3. The percentage of votes each candidate received
#    4. Determine the winner with the highest number of votes


def proccess_voters(voters):

    voter_summary = {}

    # Loop through for voting counts
    for voter in voters:
        candidate = voter["candidate"]
        if candidate in voter_summary:
            voter_summary[candidate]["votes"] += 1
        else:
            voter_summary[candidate] = {"votes": 1}

    # Loop through to get vote % and the winner with highest count
    winner = ""
    vote_count = 0
    for candidate in voter_summary:
        votes = voter_summary[candidate]["votes"]
        # if latest candidate has higher vote than last, could be the winner!
        if votes > vote_count:
            vote_count = votes
            winner = candidate
        percent_votes = votes / len(voters) * 100
        voter_summary[candidate].update({"percent_votes": percent_votes})

    # Make a nice dict with all the results in 1 package
    voter_summary = {"candidates": voter_summary}

    voter_summary.update({"total_votes": len(voters)})
    voter_summary.update({"winner": winner})

    return voter_summary


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

    # Get the list of voters from the csv file
    voters_list = read_voters_from_csv(read_file)

    # Get the summary breakdown of votes, %, totals, and winner
    summary_of_votes = proccess_voters(voters_list)

    # Print out into the console and file the results
    output_results(write_file, summary_of_votes)


if __name__ == "__main__":
    main()
