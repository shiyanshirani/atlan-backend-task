import gspread
from oauth2client.service_account import ServiceAccountCredentials



scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('csv-to-sheets')

def conversion():
    with open('/Users/shiyan/Desktop/project/atlan/dataset/csv_to_sheets.csv', 'r') as file:
        content = file.read()
        client.import_csv(spreadsheet.id, data=content)
    print("Conversion successful")