import argparse, csv, pathlib
from plugins import filter_slangs, monthly_savings, csv_to_sheets, send_sms

parser = argparse.ArgumentParser(
    description="Command line interface to interact with atlan's data"
)
parser.add_argument("--source", type=str, help="to get source's destination locally")
parser.add_argument("--plugin", type=str, help="to decide which package to use")
parser.add_argument(
    "--output", type=str, help="to deliver the output in desired format"
)
args = parser.parse_args()

source = args.source
plugin = args.plugin
output = args.output

plugins = {
    "filter_slangs": filter_slangs.slangs_func,
    "monthly_savings": monthly_savings.calculate,
    "csv_to_sheets": csv_to_sheets.generate_google_sheets,
    "send_sms": send_sms.send_notification,
}


def open_file(filepath, plugin, output):
    plugins[plugin](filepath, output)


if __name__ == "__main__":
    open_file(source, plugin, output)
