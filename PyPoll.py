#import libraries
import os
import csv

#set file path 
csvpath = os.path.join("Resources", "election_data.csv")

#create counters
votes = 0
winning = 0
#create list without headers
data = []
#create list of candidates
candidates = []
#create dictionaries of candidate votes  & percentage of votes
candidate_vote = {}
candidate_percent = {}

#open the CSV
with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        data = list(csvreader)

#loop thorugh to count the votes and get candidate names
for row in data:
        #count the number of votes
        votes = votes + 1
        #condition to append unique candidate and get count of votes
        if row[2] not in candidates:
                candidates.append(row[2])
                candidate_vote[row[2]] = 0
        candidate_vote[row[2]] = candidate_vote[row[2]] + 1

#Find count of votes for each candiate
for (key, value) in candidate_vote.items():
    candidate_percent[key] = round(value/votes * 100, 1)
    if winning < value:
        winning = value
        elected_candidate = key

#print out the results of the election
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")
for (key,value) in candidate_vote.items():
        print(f'{key}: {candidate_percent[key]}% ({value})')
print("-------------------------")
print("Winner: " + elected_candidate)
print("-------------------------")

# Specify the file to write to
output_path = os.path.join("pypoll_output.txt")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    #print the election results
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Total Votes: ' + str(votes)])
    csvwriter.writerow(['-------------------------'])
    for (key,value) in candidate_vote.items():
        csvwriter.writerow([f'{key}: {candidate_percent[key]}% ({value})'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Winner: ' + elected_candidate])
    csvwriter.writerow(['-------------------------'])