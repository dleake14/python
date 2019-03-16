import csv

with open('data.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('data.csv', 'w+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Name', 'Age','Hair Color'))
        writer.writerows(lines)
        writer.writerows(('=sum(b2:b4)'))
