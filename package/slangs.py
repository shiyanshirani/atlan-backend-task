import csv

def slangsFunc(file, output):
    reader = csv.reader(file)
    for row in reader:
        if row[4][-1:] == "n":
            with open(f'{output}.csv', 'a', newline='') as file:
                fieldnames = ['name', 'phone', 'email', 'city', 'slang']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                writer.writerow(
                    {
                        "name": row[0],
                        "phone": row[1],
                        "email": row[2],
                        "city": row[3],
                        "slang": row[4] 
                    }
                )
    print(f"{output}.csv file generated")