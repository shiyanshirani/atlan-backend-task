import argparse, csv, pathlib
from package import slangs

# cli args
parser = argparse.ArgumentParser(description="Command line interface to interact with atlan's data")
parser.add_argument('--source', type=str, help="to get source's destination locally")
parser.add_argument('--plugin', type=str, help="to decide which package to use")
parser.add_argument('--output', type=str, help="to deliver the output in csv file")
args = parser.parse_args()
path = args.source


with open('dataset/slangs.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    