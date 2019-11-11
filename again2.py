import csv

with open('MobilePhoneMasts.csv', 'rt') as csvfile:
    # handle header line, save it for writing to output file
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    results = filter(lambda row: row[1] != 'Mac' and int(row[2]) > 20, reader)
    print(results)
