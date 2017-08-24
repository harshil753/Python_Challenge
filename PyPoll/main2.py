import os
import csv

csvone = os.path.join('Resources','election_data_1.csv')
csvtwo = os.path.join('Resources','election_data_2.csv')

total = 0 
candidate=""
clist = []
votes = []
percentage =[]

totals = zip(clist, votes, percentage)
with open(csvone, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    for row in csvreader:
        total = total +1
        candidate = row[2]
        if not candidate in clist:
            clist.append(candidate)
        elif candidate in clist:
            votes[clist.index(candidate)] = int(votes[clist.index(candidate)]) + 1


