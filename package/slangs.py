import csv

def slangs(file):
    reader = csv.reader(file)
    for row in reader:
        if row[4][-1:] == "n":
            print(row)