def conversion():
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/shiyan/Desktop/project/atlan/package/client_secret.json', scope)
    client = gspread.authorize(credentials)

    spreadsheet = client.open('csv-to-sheets')

    with open('/Users/shiyan/Desktop/project/atlan/dataset/csv_to_sheets.csv', 'r') as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)
        
    print('Conversion Successfull')