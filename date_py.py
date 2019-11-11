# import csv
# from datetime import datetime

# with open('MobilePhoneMasts.csv') as fp:
#     reader = csv.reader(fp)
#     next(reader) # skip header
#     for row in reader:
#         row = [int(r) for r in row]
#         print(datetime(row[0])) # , row[1], row[2], row[3], row[4]
#!/usr/bin/env python3

# import csv

# with open('MobilePhoneMasts.csv', newline='') as csvfile:
#     data = csv.reader(csvfile, delimiter=';')
#     transposed = list(zip(*data))
#     print(transposed)
import csv
from datetime import datetime

class MyClass():

    def convert_csv_date(csv_date):
      return datetime.strptime(csv_date, "%d %b %Y").strftime("%d/%m/%Y")

    with open('MobilePhoneMasts.csv', 'r') as csvfile:
	    data = csv.reader(csvfile, delimiter=';')
	    included_cols = [7]
	    x = [[rows[0]] for rows in data]
	    x1 = [[row[0].split(',')[7] for row in x]]
	    # x2 = [[row[0].split(',')[1] for row in x]]
	    # x3 = [[row[0].split(',')[7] for row in x]]
	    # for x in x1:
	    print(datetime(x1))
	    # [['4', '7', '3', '3']]

	    # print(x2)
	    # # [['9', '11', '5', '6']]

	    # print(x3)
	    # # [['5', '4', '2', '3']]