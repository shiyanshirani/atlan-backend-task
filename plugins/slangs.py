import csv

def slangs_func(filepath, output):
    with open(f'{filepath}') as file:
        with open(f'output/{output}', 'a', newline='') as newfile:
            fieldnames = ['name', 'phone', 'email', 'city', 'slang']
            writer = csv.DictWriter(newfile, fieldnames=fieldnames)
            writer.writeheader()
            reader = csv.reader(file)
            for row in reader:
                if row[4][-1:] == 'n':
                        writer.writerow(
                            {
                                "name": row[0],
                                "phone": row[1],
                                "email": row[2],
                                "city": row[3],
                                "slang": row[4],
                            }
                        )

    print(f"{output}.csv file generated.")