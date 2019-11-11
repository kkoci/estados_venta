import csv
import arrow
from datetime import datetime

with open('MobilePhoneMasts.csv', 'r', newline='') as fin: 
    #inp = row["21 apr 2015"]
    out = datetime.strptime(inp, "%d %b %Y")
    #print(out.strftime("%d/%m/%Y"))
        reader = csv.reader(fin)
        #writer = csv.writer(fout)
        for row in reader:
            row[7] = datetime.strptime(row[7], ).strftime('%m%d‌​%Y')
            #writer.writerow(row)
            print(reader)
