import pandas as pds
import numpy as np
from numpy import corrcoef, sum, log, arange
from pylab import pcolor, show, colorbar, xticks, yticks
import os

cwd = os.getcwd() + '/'

df = pds.read_csv(cwd + 'keplerConfirmed.csv')
dc = df.corr()

# plotting the correlation matrix
pcolor(dc)
colorbar()
yticks(arange(0.5,10.5),range(0,10))
xticks(arange(0.5,10.5),range(0,10))
show()
