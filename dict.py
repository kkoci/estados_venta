import csv

with open('MobilePhoneMasts.csv', mode='r') as infile:
    reader = csv.reader(infile)
    #with open('coors_new.csv', mode='w') as outfile:
    # writer = csv.writer(outfile)
    mydict = {rows[6]:rows[1] for rows in reader}
    total = sum(float(row[0]) for row in mydict)
    print(mydict,  "The total is %s" % total)