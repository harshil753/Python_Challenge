import os
import csv

csvone = os.path.join('Resources', 'election_data_1.csv')
csvtwo = os.path.join('Resources', 'election_data_2.csv')

total = int(0)
totaltwo = int(0)

candidate = ""
candidatetwo = ""

clist = []
clisttwo=[]

candidate_total = int(0)
candidate_totaltwo= int(0)

voteone=int(0)
votetwo=int(0)
votethree=int(0)
votefour=int(0)
votefive=int(0)
votesix=int(0)
voteseven=int(0)
voteeight=int(0)

percent_one = float(0)
percent_two = float(0)
percent_three = float(0)
percent_four = float(0)
percent_five = float(0)
percent_six = float(0)
percent_seven = float(0)
percent_eight = float(0)

with open(csvone, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    for row in csvreader:
        total = total +1
        candidate = row[2]
        if not candidate in clist:
            clist.append(candidate)
        if candidate == clist[0]:
            voteone =voteone +1
        elif candidate == clist[1]:
            votetwo = votetwo +1
        elif candidate == clist[2]:
            votethree = votethree+1
        elif candidate == clist[3]:
            votefour = votefour+1
    percent_one = voteone/total *100
    percent_two = votetwo/total *100
    percent_three = votethree/total *100                   
    percent_four = votefour/total *100                   
                   
print("Election Results")
print("________________")
print ("Total votes cast:",total)
print("________________")
print(clist[0]+":",percent_one,"%",voteone)
print(clist[1]+":",percent_two,"%",votetwo)
print(clist[2]+":",percent_three,"%",votethree)
print(clist[3]+":",percent_four,"%",votefour)
print("________________")
if voteone> max(votetwo, votethree, votefour):
    print("Winner:",clist[0])
if votetwo> max(voteone, votethree, votefour):
    print("Winner:",clist[1])
if votethree> max(votetwo, voteone, votefour):
    print("Winner:",clist[2])
if votefour> max(votetwo, votethree, voteone):
    print("Winner:",clist[3])

with open(csvtwo, newline="") as csvfiletwo:
    csvreadertwo = csv.reader(csvfiletwo, delimiter=",")
    next(csvreadertwo, None)
    for row in csvreadertwo:
        totaltwo = totaltwo+1
        candidatetwo = row[2]
        if not candidatetwo in clisttwo:
            clisttwo.append(candidatetwo)
        if candidatetwo == clisttwo[0]:
            votefive =votefive+1
        elif candidatetwo == clisttwo[1]:
            votesix = votesix+1
        elif candidatetwo == clisttwo[2]:
            voteseven = voteseven+1
        elif candidatetwo == clisttwo[3]:
            voteeight = voteeight+1
        percent_five = (votefive/totaltwo) *100
        percent_six = (votesix/totaltwo) *100
        percent_seven = (voteseven/totaltwo) *100
        percent_eight = (voteeight/totaltwo) *100

print("Election 2 Results")
print("________________")
print ("Total votes cast:",totaltwo)
print("________________")
print(clisttwo[0]+":",percent_five,"%",votefive)
print(clisttwo[1]+":",percent_six,"%",votesix)
print(clisttwo[2]+":",percent_seven,"%",voteseven)
print(clisttwo[3]+":",percent_eight,"%",voteeight)
print("________________")
if votefive> max(votesix, voteseven, voteeight):
    print("Winner:",clist[0])
if votesix> max(votefive, voteseven, voteeight):
    print("Winner:",clist[1])
if voteseven> max(votesix, votefive, voteeight):
    print("Winner:",clist[2])
if voteeight> max(votefive, votesix, voteseven):
    print("Winner:",clist[3])


