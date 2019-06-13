#import libraries
import os
import csv

#set file path 
csvpath = os.path.join("Resources", "election_data.csv")

#create counter(s)
votes = 0
winning = 0
#create list without headers
data = []
#create list of candidates
candidates = []
#create dictionary of candidate & vote count
candidate_vote = {}
candidate_percent = {}

#open the CSV
with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        data = list(csvreader)

for row in data:
        #count the number of votes
        votes = votes + 1
        #condition to append unique candidate and get count of votes
        if row[2] not in candidates:
                candidates.append(row[2])
                candidate_vote[row[2]] = 0
        candidate_vote[row[2]] = candidate_vote[row[2]] + 1
#Find count of votes for each candiate / total votes (i.e. votes) * 100 = % of votes
#Find count votes for each candiate
for (key, value) in candidate_vote.items():
    candidate_percent[key] = round(value/votes * 100, 1)
    if winning < value:
        winning = value
        elected_candidate = key

for (key,value) in candidate_vote.items():
        print(f'{key} {candidate_percent[key]} {value}')

#print(data)
print("Total Votes: " + str(votes))
print(candidates)
print(candidate_vote)
print(candidate_percent)
print(elected_candidate)
print(winning)
