import csv

# Indices for list with no planets
NONEMETAL = 10
NONETEMP = 6
NONERAD = 12
NONEMASS = 13

# Indices for confirmed
CONMETAL = 15
CONTEMP = 7
CONRAD = 19
CONMASS = 22

# Put rows into lists to make them easier to deal with
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
		if row[0][0]!='#':
			print row
			break
	for row in reader:
		confirmedPlanets.append(row)

noPlanetsGraph = []
confirmedGraph = []
for x in noPlanets:
	noPlanetsGraph.append(float, [x[NONETEMP], x[NONEMETAL], x[NONERAD], x[NONEMASS]])
for x in confirmedPlanets:
	noPlanetsGraph.append(float, [x[NONETEMP], x[NONEMETAL], x[NONERAD], x[NONEMASS]])
