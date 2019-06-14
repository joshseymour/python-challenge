import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

total_votes = 0
candidates = []
count_votes= []
cand_vote_count = {}
cand_perc = {}
winning_count = 0


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader: 
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            cand_vote_count[row[2]] = 0
        cand_vote_count[row[2]] += 1   

for (key, value) in cand_vote_count.items():
    cand_perc[key] = round(value/total_votes * 100, 0)
    if winning_count < value:
        winning_count = value
        Winner = key

print(len(str(total_votes)))
print(candidates)
print(cand_vote_count)
print(cand_perc)
print(Winner)
print(winning_count)