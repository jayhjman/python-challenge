# Banking Profits/Losses and Election Results

- _*Banking Profits/Losses*_ - Python program that analyzes the financial records of the given bank from Jan-2010 to Feb-2017 ([see data](PyBank/Resources/budget_data.csv)) . The purpose is show how many months the analysis covers, the total amount profit/losses, average change month over month, greatest monthly increase, and the greatest monthly decrease.

- _*Election Results*_ - Python program that analyzes the election voter records for the given candidates ([see data](PyPoll/Resources/election_data.csv)). The purpose is show who won the election, the percentage and total breakdown of votes for each candidate, and final overall total vote count.

## Files

- Banking Files

  - [Banking Data](PyBank/Resources/budget_data.csv) - Source file for the banking data to be processed

  - [main.py](PyBank/main.py) - The python code for processing the [Banking Data](PyBank/Resources/budget_data.csv)

- Election Files

  - [Election Data](PyPoll/Resources/election_data.csv) - Source file for the banking data to be processed

  - [main.py](PyPoll/main.py) - The python code for processing the [Election Data](PyPoll/Resources/election_data.csv)

## Results

- [Banking Results](PyBank/analysis/results.txt)

```
Financial Analysis
--------------------------------------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 $(1926159)
Greatest Decrease in Profits: Sep-2013 $(-2196167)
--------------------------------------------------------
```

- [Election Results](PyPoll/analysis/results.txt)

```
Election Results
-------------------------------
Total Votes: 3521001
-------------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------------
Winner: Khan
-------------------------------
```

## Execution

1. The assumption is that you have a working Python 3.6 environment
1. Clone the [`git repository`](https://github.com/jayhjman/python-challenge) for this project
1. Change into the [`repository directory`](https://github.com/jayhjman/python-challenge) and then into [`PyBank`](PyBank/) or [`PyPoll`](PyPoll/)
1. Execute `main.py` via command line in the following manner `python main.py`
1. This will execute against the `csv` file found under either [`PyBank`](PyBank/Resources/) or [`PyPoll`](PyPoll/Resources/) `Resources` directory
1. Results can be found under the `analysis` directory for [`PyBank`](PyBank/analysis/) or [`PyPoll`](PyPoll/analysis/)

## Author

Made by Jay with :heart: in 2020.
