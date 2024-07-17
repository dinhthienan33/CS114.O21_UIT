import csv

with open('2.csv', 'r') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
    f.close()
with open('2.csv', 'w',newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row + [''])
    f.close()