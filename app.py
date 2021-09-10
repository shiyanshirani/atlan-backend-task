import argparse, csv, pathlib
from plugins import slangs, monthly_savings, csv_to_sheets, send_sms


# CLI ARGUMENTS
parser = argparse.ArgumentParser(description="Command line interface to interact with atlan's data")
parser.add_argument('--source', type=str, help="to get source's destination locally")
parser.add_argument('--plugin', type=str, help="to decide which package to use")
parser.add_argument('--output', type=str, help="to deliver the output in desired format")
args = parser.parse_args()

source = args.source
plugin = args.plugin
output = args.output

dispatch_table = {
    'slangs': slangs.slangs_func,
    'monthly_savings': monthly_savings.calculate,
    'csv_to_sheets': csv_to_sheets.conversion,
    'send_sms': send_sms.send_notification
}


def openFile(filepath, plugin, output):
    # if plugin == "slangs":
    #     slangs.slangs_func(filepath, output)
    # elif plugin == "monthly_savings":
    #     monthly_savings.calculate(filepath, output)
    # elif plugin == 'csv_to_sheets':
    #     csv_to_sheets.conversion(filepath)
    # elif plugin == 'send_sms':
    #     send_sms.sendNotification(filepath)
    dispatch_table[plugin](filepath, output)


if __name__ == "__main__":
    openFile(source, plugin, output)