import os
import csv
import operator

# Path to collect data from the Resources folder
pollCSV = os.path.join("Resources", "election_data.csv")
file_output = open("Output//pypoll_output.txt","w")

# Function to calculate vote
def calculate_Vote(dict_polls, total_vote):
    for k, v in dict_polls.items():
        percent_vote = round(v/(int(total_vote))*100,3)
        val = "{0:.3f}".format(percent_vote)
        file_output.write(f'{k} : {val}% ({v})' + "\n")
    file_output.write("----------------------------" + "\n")
    file_output.write("Winner: " + max(dict_polls.keys(), key=(lambda k: dict_polls[k])) + "\n")
    file_output.write("----------------------------" + "\n")

# Read in the CSV file
with open(pollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_votes = 0
    
    dict_poll = dict()
    # Loop through the data
    for row in csvreader:
        total_votes = total_votes + 1
        per_vote = 1
        #if candidate key already exist just added the count of vote
        if row[2] in dict_poll.keys():
            dict_poll[row[2]] = dict_poll.get(row[2]) + per_vote
        else:
            dict_poll[row[2]] = per_vote

    #write to output file
    file_output.write("Election Results" +"\n")
    file_output.write("----------------------------" + "\n")
    file_output.write(f' Total Votes: {total_votes} ' + "\n")
    file_output.write("----------------------------" + "\n")
    calculate_Vote(dict_poll,total_votes)
    
    file_output.close()