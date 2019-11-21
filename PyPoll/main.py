import os
import csv

PyPoll_csv = os.path.join("Resources","election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(PyPoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        count = count + 1
        candidatelist.append(row[2])
    for i in set(candidatelist):
        unique_candidate.append(i)
        y = candidatelist.count(i)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for j in range(len(unique_candidate)):
            print(unique_candidate[j] + ": " + str(round(vote_percent[j],3)) +"% (" + str(vote_count[j])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")



with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("-------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("-------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("-------------------------\n")