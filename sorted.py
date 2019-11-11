import csv
with open('MobilePhoneMasts.csv', 'r') as f:
    reader = csv.reader(f)
    d = {}
    for row in f:
        row = row.split(",")
        d[row[0]]=(row[1]) 
k = sorted(d, key=d.__getitem__, reverse=True)
v = sorted(d.values(), reverse=True)
sorted_d = zip(k,v)
print (sorted_d)
