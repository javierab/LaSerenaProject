import os
import sys
from astroquery.vizier import VizierClass
from astropy.coordinates import Angle

cwd = os.getcwd() + '/'
NAME = sys.argv[1]
print NAME

if not os.path.exists(NAME):
	os.makedirs(NAME)

ucd = '(phys.temperature.effective|phys.gravity|phys.abund.Z|phys.veloc.rotat|time.period|time.age|spect.dopplerVeloc*|src.var|src.var.index|meta.code.multip)'

vizier = VizierClass(ucd = ucd, columns = ['Teff', 'logg','vsini', '[Fe/H]', 'M', 'Period', 'Vmag'])

result = vizier.query_object(NAME, radius = Angle(0.00014, 'deg'))

i = 0
for table in result:
	table.write(open(NAME +'/' + NAME + '-'+str(i) + '.csv','w+'), format = 'csv')
	i+=1
