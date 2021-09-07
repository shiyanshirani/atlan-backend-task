import csv
from time import time 
from faker import Faker

fake = Faker('en_US')
RECORD_COUNT = 1000
MONTHLY_INCOME = 200000

# Function to create fake data and storing them in a file
def create_slangs(filename):
    with open(filename+".csv", 'w', newline="") as file:
        fieldnames = ['name', 'phone', 'email', 'city', 'slang']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    "name": fake.name(),
                    "phone": fake.phone_number(),
                    "email": fake.email(),
                    "city": fake.city(),
                    "slang": fake.word()
                }
            )

def createCSVSampleData(filename):
    with open(filename+".csv", 'w', newline="") as file:
        fieldnames = ['name', 'phone', 'dob', 'email', 'city', 'address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    "name": fake.name(),
                    "phone": fake.phone_number(),
                    "dob": fake.date_of_birth(),
                    "email": fake.email(),
                    "city": fake.city(),
                    "address": fake.address()
                }
            )

def create_monthlySavings(filename):
    with open(filename+".csv", 'w', newline="") as file:
        fieldnames = ['name', 'age', 'phone', 'email', 'address', 'monthly_savings']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    "name": fake.name(),
                    "age": fake.random_int(min=1, max=80),
                    "phone": fake.phone_number(),
                    "email": fake.email(),
                    "address": fake.street_address(),
                    "monthly_savings": fake.random_int(min=50000, max=400000)
                }
            )

def sendSMSData(filename):
    with open(filename+".csv", 'w', newline="") as file:
        fieldnames = ['name', 'age', 'phone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(10):
            writer.writerow(
                {
                    "name": fake.name(),
                    "age": fake.random_int(min=1, max=80),
                    "phone": fake.phone_number(),
                }
            )

if __name__ == '__main__':
    print("Which data do you want to produce:")
    var = int(input("1: slangs 2: monthly_savings 3: csv_to_sheets  4: send_sms   -> "))
    start = time() # Time start
    if var == 1:
        create_slangs("slangs")
    elif var == 2:
        create_monthlySavings("monthly_savings")
    elif var == 3:
        createCSVSampleData('csv_to_sheets')
    else:
        sendSMSData('send_sms_data')
        
    total_time = time() - start # Time stop
    total_time = str(total_time)[:7]
    print(f"csv_file created in {total_time}s")