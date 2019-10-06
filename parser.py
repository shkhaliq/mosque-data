import csv
from datetime import date
import glob
import os
import json

this_month = date.today().strftime("%B")
this_day = date.today().day

def parse_csv(csvFile):
    with open(csvFile) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            row = { x.replace(u'\xa0', u' '): v for x, v in row.items() } 
            if line_count == 0:
                line_count += 1
            elif row["Day"] == str(this_day):
                r = json.dumps(row)
                print(r)
            else:
                line_count += 1
        print(f'Processed {line_count} lines.')


cwd = os.getcwd()
os.chdir('prayer-times/')
for file in glob.glob("**/*.csv"):
    if this_month in file:
        print(os.path.dirname(file))
        parse_csv(file)

os.chdir(cwd)