# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 12:27:31 2015

@author: mmoshe
"""

import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid

delta = 0.025
xrange = arange(-5.0, 5.0, delta)
yrange = arange(-5.0, 5.0, delta)
X, Y = meshgrid(xrange,yrange)

# F is one side of the equation, G is the other
F = Y**2
G = -X*(X-1)*(X-2)

matplotlib.pyplot.contour(X, Y, (F + G), [0])
matplotlib.pyplot.show()