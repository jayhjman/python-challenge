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
    winner = ""
    vote_count = 0
    for candidate in voter_summary.keys():
        votes = voter_summary[candidate]["votes"]
        if votes > vote_count:
            vote_count = votes
            winner = candidate
        percent_votes = votes / len(voters) * 100
        voter_summary[candidate].update({"percent_votes": percent_votes})

    voter_summary = {"candidates": voter_summary}

    voter_summary.update({"total_votes": len(voters)})
    voter_summary.update({"winner": winner})

    return voter_summary


def output_results(output_file, summary):

    string_to_output = 'Election Results\n'
    string_to_output += '-------------------------------\n'
    string_to_output += str.format(f'Total Votes: {summary["total_votes"]}\n')
    string_to_output += '-------------------------------\n'
    candidates = summary["candidates"]
    for candidate in candidates:
        candidate_info = candidates[candidate]
        string_to_output += str.format(
            f'{candidate}: {candidate_info["percent_votes"]:.3f}% ({candidate_info["votes"]})\n')
    string_to_output += '-------------------------------\n'

    # Print out the summary table
    print(string_to_output)

    # Write the output results text file
    results_file = open(output_file, 'w')
    num_of_chars = results_file.write(string_to_output)
    results_file.close()


def main():

    # Find the path of the current file
    source_path = os.path.dirname(os.path.abspath(__file__))

    # Create read/write file paths with file names
    read_file = os.path.join(source_path, 'Resources', 'election_data.csv')
    write_file = os.path.join(source_path, 'analysis', 'results.txt')

    voters_list = read_voters_from_csv(read_file)

    summary_of_votes = proccess_voters(voters_list)

    output_results(write_file, summary_of_votes)


if __name__ == "__main__":
    main()
