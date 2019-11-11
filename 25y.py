import operator
import csv

filename = "MobilePhoneMasts.csv"
def load_source(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=";")
        return filter(lambda x: x[12] in ("25 years"), list(reader))
