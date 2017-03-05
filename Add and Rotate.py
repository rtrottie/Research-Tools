__author__ = 'Ryan'
from math import pi
import random


location = [0.42719,  0.75,  0.25]
yaw = pi/2
pitch = pi/4
roll = pi/2

# Work Computer
baseLocation = 'D:\\Users\\Ryan\\Documents\\Scrap\\plain\\surface\\CONTCAR'
# moleculeLocation = 'D:\\Users\\Ryan\\Google Drive CU\\Python\\Research-Tools\\Molecules\\PEROXIDE'
# saveLocation = 'D:\\Users\\Ryan\\Documents\\Scrap\\POSCAR'

# baseLocation = 'D:\\My Stuff\\GoogleDrive_CU\\Python\\Research-Tools\\Surfaces\\TiO2\\TIO2_SMALL'
moleculeLocation = 'D:\\Users\\Ryan\\Documents\\Scrap\\molecules\\BPA\\CONTCAR'
saveLocation = 'D:\\Users\\Ryan\\Documents\\scrap\\POSCAR'



location = NP.matrix(location)
roll = NP.longdouble(roll)
pitch = NP.longdouble(pitch)
yaw = NP.longdouble(yaw)

base = loadPosFile(baseLocation)
molecule = loadPosFile(moleculeLocation)


savePosfile(addAndRotate(base,molecule,location, roll, pitch, yaw), saveLocation)