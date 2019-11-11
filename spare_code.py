
def fst_func():
try:
    with open('Mycsv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for i,row in enumerate(reader):
            rowlist = [row['1st row'], row['2nd row'], row['3rd row'], row['4th row'], row['5th row']]
            print(sorted(rowlist))
            if(i >= 4):
                break



import csv
from datetime import datetime

class MyClass():

    def convert_csv_date(csv_date):
      return datetime.strptime(csv_date, "%d %b %Y").strftime("%d/%m/%Y")


    lines = [['Vacation_Days', 'Date'],
     ['New Years', '01 jan 2019'],
     ['Labor Day', '02 sep 2019'],
     ['Thanksgiving', '24 nov 2019']]

    with open('/tmp/output.csv', 'w') as writer:
        fd = csv.writer(writer)
        fd.writerows(lines)

    r = csv.reader(open('/tmp/output.csv')) # Here's a sample date csv file
    lines = list(r)

    for item in lines[1:]: 
       item[1] = convert_csv_date(str(item[1])) 

    print(lines)

    with open('/tmp/output_test.csv', 'w') as writer:
        fd = csv.writer(writer)
        fd.writerows(lines)