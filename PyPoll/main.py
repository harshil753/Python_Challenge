import os
import csv

csvone = os.path.join('Resources', 'election_data_1.csv')


total = int(0)

candidate = ""

clist = []

candidate_total = int(0)

voteone=int(0)
votetwo=int(0)
votethree=int(0)
votefour=int(0)


percent_one = float(0)
percent_two = float(0)
percent_three = float(0)
percent_four = float(0)

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

file = open("Election Results.txt", "w")
file.write("Election Results"+'\n')
file.write("________________"+'\n')
file.write("Total votes cast: "+str(total)+'\n')
file.write("________________"+'\n')
file.write(clist[0]+": "+str(percent_one)+"% "+str(voteone)+'\n')
file.write(clist[1]+":"+str(percent_two)+"% "+str(votetwo)+'\n')
file.write(clist[2]+": "+str(percent_three)+"% "+str(votethree)+'\n')
file.write(clist[3]+": "+str(percent_four)+"% "+str(votefour)+'\n')
file.write("________________"+'\n')
if voteone> max(votetwo, votethree, votefour):
    file.write("Winner: "+clist[0]+'\n')
if votetwo> max(voteone, votethree, votefour):
    file.write("Winner: "+clist[1]+'\n')
if votethree> max(votetwo, voteone, votefour):
    file.write("Winner: "+clist[2]+'\n')
if votefour> max(votetwo, votethree, voteone):
    file.write("Winner: "+clist[3]+'\n')