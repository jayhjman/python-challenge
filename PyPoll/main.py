#
# PyPoll
#
# Script that analyzes the financial records of the given bank.
# The purpose is show how many months the analysis covers, the
# total amount profit/losses, average change, greatest increase,
# and greatest decrease.
#

# Imports
import os
import csv


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


def proccess_voters(voters):

    voter_summary = {}

    # Loop through for voting counts
    for voter in voters:
        candidate = voter["candidate"]
        if candidate in voter_summary:
            voter_summary[candidate]["votes"] += 1
        else:
            voter_summary[candidate] = {"votes": 1}

    # Loop through to get vote %
    for candidate in voter_summary.keys():
        print(candidate)

    return voter_summary


def main():

    # Find the path of the current file
    source_path = os.path.dirname(os.path.abspath(__file__))

    # Create read/write file paths with file names
    read_file = os.path.join(source_path, 'Resources', 'election_data.csv')
    write_file = os.path.join(source_path, 'analysis', 'results.txt')

    voters_list = read_voters_from_csv(read_file)

    print(len(voters_list))

    summary_of_votes = proccess_voters(voters_list)

    print(summary_of_votes)


if __name__ == "__main__":
    main()
