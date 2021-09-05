import argparse, csv, pathlib
from package import slangs, monthlySavings


# cli args
parser = argparse.ArgumentParser(description="Command line interface to interact with atlan's data")
parser.add_argument('--plugin', type=str, help="to decide which package to use")
parser.add_argument('--source', type=str, help="to get source's destination locally")
parser.add_argument('--output', type=str, help="to deliver the output in csv file")
args = parser.parse_args()

source = args.source
plugin = args.plugin
output = args.output

def openFile(path, plugin, output):
    with open(path) as file:
        if plugin == "slangs":
            slangs.slangsFunc(file, output)
        elif plugin == "monthy_savings":
            monthlySavings(file, output)
        


if __name__ == "__main__":
    openFile(source, plugin, output)