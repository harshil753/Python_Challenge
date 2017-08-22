import os
import csv

csvone = os.path.join('Resources','budget_data_1.csv')
csvtwo = os.path.join('Resources','budget_data_2.csv')

months = int(0)
revenue = float(0)
average_change = float(0)
previous_revenue = float(0)
revenue_change = float(0)
high = float(0)
high_date = ""
low = float(0)
low_date = ""
with open(csvone, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    for row in csvreader:
        value = float(row[1])
        months = months+1
        revenue_change = (value-previous_revenue)
        average_change = revenue_change/months
        revenue = revenue+value
        previous_revenue = value
        if high == 0:
            high = revenue_change
            high_date = row[0]
        elif int(high) < int(revenue_change):
            high = revenue_change
            high_date = row[0]
        if low == 0:
            low = revenue_change
            low_date = row[0]
        elif int(revenue_change) < int(low):
            low = revenue_change
            low_date = row[0]
with open(csvtwo, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    for row in csvreader:
        value = float(row[1])
        months = months+1
        revenue_change = (value-previous_revenue)
        average_change = revenue_change/months
        revenue = revenue+value
        previous_revenue = value
        if high == 0:
            high = revenue_change
            high_date = row[0]
        elif int(high) < int(revenue_change):
            high = revenue_change
            high_date = row[0]
        if low == 0:
            low = revenue_change
            low_date = row[0]
        elif int(revenue_change) < int(low):
            low = revenue_change
            low_date = row[0]

print("Total months:",months)        
print("Total revenue: $"+ str(revenue))
print("Average change in revenue: $"+str(previous_revenue))
print("Highest increase in revenue:",str(high),"on",high_date)
print("Highest decrease in revenue:",str(low),"on",low_date)