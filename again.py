# import csv
# import operator
# from datetime import datetime
# from dateutil import parser

# def fst_func():
#     try:
#         with open('MobilePhoneMasts.csv') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for i,row in enumerate(reader):
#                 rowlist = (row['Tenant Name'], row['Current Rent'], row['Property Address [4]'], row['Unit Name'], row['Lease Years'])
#                 print(sorted(rowlist))
#                 if(i >= 4):
#                     break
#     except:
#         print("No such file or directory")
# #if __name__ == "__main__":
# fst_func()
# import csv
# from operator import itemgetter


# def fst_func(filename, numrows=4):
#     rows = []
#     try:
#         with open(filename) as csvfile:
#             reader = csv.DictReader(csvfile)
#             for i, row in enumerate(reader, 1):
#                 rows.append(row)
#                 if i >= numrows:
#                     break
#     except FileNotFoundError:
#         print("file {!r} does not exist".format(filename))
#         return

#     rows.sort(key=lambda row: float(itemgetter('Current Rent')(row)))
#     for row in rows:
#         print(', '.join(row.values()))

# fst_func('MobilePhoneMasts.csv')
# 
import csv

myfile = r'MobilePhoneMasts.csv'

with open(myfile, 'r', newline='') as f:
    c = csv.DictReader(f)
    filtering = [row for row in c if row['Lease Years'] == '25']

    # Rewind and skip header
    f.seek(0)
    next(f)

    total = sum(float(row["Current Rent"]) for row in filtering)
    print(filtering, "The total is %s" % total)