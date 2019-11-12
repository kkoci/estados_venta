import csv
from datetime import datetime

class MyClass():

    def convert_csv_date(csv_date):
        return datetime.strptime(csv_date, "%d %b %Y").strftime("%d/%m/%Y")

    with open('MobilePhoneMasts.csv', 'r') as infile:
        # read the file as a dictionary for each row ({header : value})
        reader = csv.DictReader(infile)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]

                # lines = [['Vacation_Days', 'Date'],
                #  ['New Years', '01 jan 2019'],
                #  ['Labor Day', '02 sep 2019'],
                #  ['Thanksgiving', '24 nov 2019']]
                lines = row['Lease Start Date']
                #var = row[]

                # for item in lines[1:]: 
                #    item[1] = convert_csv_date(str(item[1])) 

                print(datetime.strptime(lines, "%d %b %Y").strftime("%d/%m/%Y"))