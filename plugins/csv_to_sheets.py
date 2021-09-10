import gspread
from oauth2client.service_account import ServiceAccountCredentials


def generate_google_sheets(filepath, *args):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "/Users/shiyan/Desktop/project/atlan/plugins/client_secret.json",
        scope,  # Kindly use absolute path for the specific json key.
    )
    client = gspread.authorize(credentials)

    spreadsheet = client.open("csv-to-sheets")

    with open(f"{filepath}", "r") as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)

    print("Conversion Successfull")
