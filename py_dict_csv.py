import csv

reader = csv.DictReader(open('MobilePhoneMasts.csv'))
result = {}
#with open('MobilePhoneMasts.csv') as f:

    #next(f) #for skipping first row in the file
    #myTuples = [] #store tuples from col1 and col2
for row in reader:
    #myTuples.append(tuple([row[0], row[1]])) #append col1 and col 2 to myTuples
    #for row in reader:
    result[row['Tenant Name']] = row['Current Rent']
    #result = dict(myTuples)
    print(result)
