import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import numpy

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
		#print row
		break
	for row in reader:
		noPlanets.append(row)


confirmedPlanets = []
with open(cwd + 'keplerConfirmed.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if row[0][0]!='#':
			#print row
			break
	for row in reader:
		confirmedPlanets.append(row)

# Put relevant data into lists for graphing
noPlanetsGraph = [[] for i in range(4)]
confirmedGraph = [[] for i in range(4)]
print "go"
for x in noPlanets:
	if len(x[0]) > 15:		# Newest data release
		noPlanetsGraph[0].append(float(x[NONETEMP]))
		noPlanetsGraph[1].append(numpy.power(10, float(x[NONEMETAL])))
		noPlanetsGraph[2].append(float(x[NONERAD]))
		#noPlanetsGraph[3].append(float(x[NONEMASS]))
for x in confirmedPlanets:
	if len(x[1]) > 15:
		confirmedGraph[0].append(float(x[CONTEMP]))
		confirmedGraph[1].append(numpy.power(10,float(x[CONMETAL])))
		confirmedGraph[2].append(float(x[CONRAD]))
		#confirmedGraph[3].append(float(x[CONMASS]))
# 2D
plt.scatter(noPlanetsGraph[0], noPlanetsGraph[1], c='r')
plt.scatter(confirmedGraph[0], confirmedGraph[1], c='b')

# 3D
'''fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(noPlanetsGraph[0], noPlanetsGraph[1], zs = noPlanetsGraph[2], c='r')
ax.scatter(confirmedGraph[0], confirmedGraph[1], zs = confirmedGraph[2], c='b')'''

plt.show()