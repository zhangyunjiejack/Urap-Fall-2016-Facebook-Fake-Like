import csv
import sys
csv.field_size_limit(500 * 1024 * 1024)
likes = []
with open('profile_likes_excel.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['likes'])
    