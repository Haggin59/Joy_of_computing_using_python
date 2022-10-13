import csv
with open('temp.csv','r') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row[0],end=" ")
        print(row[1],end=" ")
        print(row[2])