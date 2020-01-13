## woorking activity.py

import csv

reader = csv.DictReader(open("data.csv", mode="r", encoding='utf-8-sig'))

for row in reader:
	print(row)

