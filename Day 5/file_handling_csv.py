import csv

filename = "new_report.txt"

with open(filename,'w') as csvfile:
    csvreader = csv.reader(csvfile)

print(csvreader)

