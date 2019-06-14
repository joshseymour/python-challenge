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
        

