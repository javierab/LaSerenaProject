import csv

noPlanets = []
with open('/Users/Sean/Desktop/keplerNone.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print row
		break
	for row in reader:
		noPlanets.append(row)


confirmedPlanets = []
with open('/Users/Sean/Desktop/keplerConfirmed.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print row
		break
	for row in reader:
		confirmedPlanets.append(row)

