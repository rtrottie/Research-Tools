__author__ = 'Ryan'
from math import pi
import random
from helpers import *


location = [0.37085,  0.38766,  0.8]
yaw = pi/2
pitch = 0
roll = -pi

# baseLocation = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\SpinelSurface\\FeAl2'
# moleculeLocation = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\Molecules\\WATER'
# saveLocation = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\POSCAR'

baseLocation = 'C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\TiO2Surface\\TiO2_SMALL'
moleculeLocation = 'C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\Molecules\\ACETYLENE'
saveLocation = 'C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\POSCAR'

location = NP.matrix(location)
roll = NP.longdouble(roll)
pitch = NP.longdouble(pitch)
yaw = NP.longdouble(yaw)

base = loadPosFile(baseLocation)
molecule = loadPosFile(moleculeLocation)


savePosfile(addAndRotate(base,molecule,location, roll, pitch, yaw), saveLocation)