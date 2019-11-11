import csv
import codecs

def sum_csv():
    with open("MobilePhoneMasts.csv", encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        # reader = csv.reader(codecs.itercode(csv_file, 'utf-8'))
        total = sum(float(row["Current Rent"]) for row in reader)
    print(total)
sum_csv()

import itertools
import csv

with open('MobilePhoneMasts.csv', 'r', newline='') as f:
    c = csv.reader(f, delimiter=',')
    c1, c2 = tee(c)  # Split into 2 separate iterables

    # Use the first iterable, c1
    i = next(c1).index('Lease Years')
    filtering = [row for row in c1 if row[i] == '25']

    # Use a different iterable, c2
    total = sum(float(row["Current Rent"]) for row in c2)
    print(filtering, "The total is %s" % total)


import csv
import pdb

temp = r'MobilePhoneMasts.csv'

with open(temp, 'r', newline='') as f:
    cr = csv.reader(f, delimiter=',')
    # next(cr) gets the header row (row[0])
    i = next(cr).index('Lease Years')
    #u = next(cr).index('Current Rent')
    # list comprehension through remaining cr iterables
    filtered = [row for row in cr if row[i] == '25']
    pdb.set_trace()
    total = sum(float(row["Current Rent"]) for row in cr)
    print(filtered, "The total is %s" % total)#(filtered)