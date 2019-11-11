import csv

myfile = r'MobilePhoneMasts.csv'

with open(myfile, 'r', newline='') as f:
    c = csv.reader(f, delimiter=',')
    i = next(c).index('Lease Years')
    filtering = [row for row in c if row[i] == '25']

    f.seek(0)   # Rewind the file to the beginning
    next(c)     # Skip the header row

    total = sum(float(row["Current Rent"]) for row in c)
    print(filtering, "The total is %s" % total)

import csv

myfile = r'csvlist.csv'

with open(myfile, 'r', newline='') as f:
    c = csv.DictReader(f)
    filtering = [row for row in c if row['Wasted Years'] == '25']

    # Rewind and skip header
    f.seek(0)
    next(f)

    total = sum(float(row["Prices"]) for row in c)
    print(filtering, "The total is %s" % total)