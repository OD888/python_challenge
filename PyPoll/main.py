# Marc Omar Haddad
# October 4, 2019
# UNCC Data Analytics Bootcamp
# Python Challenge: PyPoll

# This program reads and tallies the votes of an election from a csv file, determines the winner, and writes a text file displaying the results


import os
import csv


def main():
    # Initializes variables
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    tooley_votes = 0
    win = 0

    # Defines path to document
    infile = os.path.join("election_data.csv")
    # Opens infile in 'read' mode
    with open(infile, 'r') as in_file:
        # Converts file to a dict of strings
        reader = csv.DictReader(in_file)
        # Iterates over dict
        for row in reader:
            candidate = row['Candidate']
            # Reads and compares each dict entry and tallies each candidate's votes
            if candidate == 'Khan':
                khan_votes += 1
            elif candidate == 'Correy':
                correy_votes += 1
            elif candidate == 'Li':
                li_votes += 1
            else:
                tooley_votes += 1
        # Custom dictionary that pairs each candidate (keys) with their respective vote totals (values)
        can_dict = {'Correy': correy_votes, 'Khan': khan_votes, 'O\'Tooley': tooley_votes, 'Li': li_votes}
    total_votes = sum(can_dict.values())
    correy_percent = correy_votes * 100/total_votes
    khan_percent = khan_votes * 100/total_votes
    li_percent = li_votes * 100/total_votes
    tooley_percent = tooley_votes * 100/total_votes
    # Finds the max value in the dict
    win = max(can_dict.values())
    # Iterates over dict to find the candidate (key) associated with the max vote total (value)
    for can in can_dict:
        if can_dict[can] == win:
            winner = can
    # Creates a new file and writes into it
    outfile = os.path.join('election_results.txt')
    with open(outfile, 'w') as out_file:
        writer = out_file.write
        writer(
            f'''\nElection Results\n----------------------------\n   Total Votes: {total_votes}\n----------------------------\n   Correy: {correy_percent:.3f}%  ({can_dict['Correy']})\n   Khan: {khan_percent:.3f}%  ({can_dict['Khan']})\n   O\'Tooley: {tooley_percent:.3f}%  ({can_dict["O'Tooley"]})\n   Li: {li_percent:.3f}%  ({can_dict['Li']})\n----------------------------\n   Winner: {winner}\n----------------------------\n''')
    # Prints results onto user's console
    print(
        f'''\nElection Results\n----------------------------\n   Total Votes: {total_votes}\n----------------------------\n   Correy: {correy_percent:.3f}%  ({can_dict['Correy']})\n   Khan: {khan_percent:.3f}%  ({can_dict['Khan']})\n   O\'Tooley: {tooley_percent:.3f}%  ({can_dict["O'Tooley"]})\n   Li: {li_percent:.3f}%  ({can_dict['Li']})\n----------------------------\n   Winner: {winner}\n----------------------------\n''')


if __name__ == "__main__":
    main()