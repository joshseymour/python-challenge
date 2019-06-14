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

# Import libraries
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#create counter for month and budget 
month = 0
budget = 0
#create lists for change and csvreader w/o header
change = []
data = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    #create list w/o the headers
    data = list(csvreader)

#add to the counters
for row in data:
    #count the number of months
    month = month + 1
     #total profit and losses 
    budget = budget + int(row[1])

#create list of budget changes
for i in range(1,month):
    change.append(int(data[i][1]) - int(data[i-1][1]))

#create variables for average change and greatest increase/decrease in profit
total_change = sum(change)
avg_change = total_change/(month - 1)

greatest_increase = max(change)
greatest_decrease = min(change)

max_index = change.index(greatest_increase)
max_value = data[max_index + 1]

min_index = change.index(greatest_decrease)
min_value = data[min_index + 1]

#print out the results in terminal
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(month))
print("Total: " + str(budget))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + str(max_value[0]) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(min_value[0]) + " ($" + str(greatest_decrease) + ")")

# Specify the file to write to
output_path = os.path.join("pybank_output.txt")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    #print the results
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total Months: ' + str(month)])
    csvwriter.writerow(['Total: ' + str(budget)])
    csvwriter.writerow(['Average Change: $' + str(avg_change)])
    csvwriter.writerow(['Greatest Increase in Profits: ' + str(max_value[0]) + ' $' + str(greatest_increase)])
    csvwriter.writerow(['Greatest Decrease in Profits: ' + str(min_value[0]) + ' $' + str(greatest_decrease)])
        

