import csv

# open the file in universal line ending mode 
with open('MobilePhoneMasts.csv', 'r') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# extract the variables you want
lease_start_date = data['Lease Start Date']
#latitude = data['Lease End Date']
# longitude = data['longitude']
print(lease_start_date)