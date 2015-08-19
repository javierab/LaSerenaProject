import csv
import matplotlib.pyplot as plt
import os

cwd = os.getcwd() + '/'
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
with open(cwd + 'keplerNone.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print row
		break
	for row in reader:
		noPlanets.append(row)


confirmedPlanets = []
with open(cwd + 'keplerConfirmed.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if row[0][0]!='#':
			print row
			break
	for row in reader:
		confirmedPlanets.append(row)

# Put relevant data into lists for graphing
noPlanetsGraph = [[] for i in range(4)]
confirmedGraph = [[] for i in range(4)]
for x in noPlanets:
	noPlanetsGraph[0].append(float(x[NONETEMP]))
	noPlanetsGraph[1].append(float(x[NONEMETAL]))
	#noPlanetsGraph[2].append(float(x[NONERAD]))
	#noPlanetsGraph[3].append(float(x[NONEMASS]))
for x in confirmedPlanets:
	confirmedGraph[0].append(float(x[CONTEMP]))
	confirmedGraph[1].append(float(x[CONMETAL]))
	#confirmedGraph[2].append(float(x[CONRAD]))
	#confirmedGraph[3].append(float(x[CONMASS]))

plt.scatter(noPlanetsGraph[0], noPlanetsGraph[1], c='r')
plt.show()
plt.scatter(confirmedGraph[0], confirmedGraph[1], c='b')
plt.show()