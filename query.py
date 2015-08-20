import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import numpy
from astroquery.vizier import Vizier
from astropy.io.votable.tree import VOTableFile, Resource, Table, Field
from astropy.table import Table as tbl

cwd = os.getcwd() + '/'

NAME = 3
#NAME = 2

nameDict = {}
with open(cwd + 'keplerConfirmedSmall.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print row
		break
	for row in reader:
		if row[NAME]:
			if row[NAME] not in nameDict:
				nameDict[row[NAME]] = 1

for key in nameDict:
	print key
print len(nameDict)

Vizier.ucd = '(phys.temperature.effective|phys.gravity|phys.abund.Z|phys.veloc.rotat|time.period|time.age|\
			spect.dopplerVeloc*|src.var|src.var.index|meta.code.multip)'

resultsList = []
for key in nameDict:
	result = Vizier.query_object(key)
	resultsList.append(result)

table = tbl()
Table.from_table(resultsList[0][0], table)

# Create a new VOTable file...
votable = VOTableFile()
resource = Resource()
votable.resources.append(resource)

# ...with one resource...
resource.tables.append(table)

votable.to_xml("new_votable.xml")
