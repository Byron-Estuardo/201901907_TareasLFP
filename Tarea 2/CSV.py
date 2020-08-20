import csv
def csvread():
    file = open('CSVTXT.csv')
    reader = csv.reader(file)
    for row in reader:
        print(row)