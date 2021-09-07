import csv
MONTHLY_INCOME = 200000

def calculate(filepath, output):
    with open(f'{filepath}') as file:
        with open(f'output/{output}.csv', 'a') as newfile:
            fieldnames = ['name', 'age', 'phone', 'email', 'address', 'monthly_savings']
            writer = csv.DictWriter(newfile, fieldnames=fieldnames)
            writer.writeheader()
            reader = csv.reader(file)
            for row in reader:
                if row[5] > MONTHLY_INCOME: # ValueError
                    writer.writerow(
                        {
                            "name": row[0],
                            "age": row[1],
                            "phone": row[2],
                            "email": row[3],
                            "address": row[4],
                            "monthly_savings": row[5],
                        }
                    )
    print(f'{output}.csv file generated')