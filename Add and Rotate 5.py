__author__ = 'Ryan'
from math import pi
import random
import os
from helpers import *


aPts = [0.415, 0.35, 0.50]
bPts = [-0.06]
cPts = [0.72, 0.53, 0.49, 0.28]

yaws = [0, pi/2]
pitchs = [0, pi/2]
rolls = [0, pi/4]



baseLocation = 'D:\\Users\\Ryan\\Google Drive CU\\Python\\Research-Tools\\Surfaces\\TiO2\\TIO2_SMALL'
moleculeLocation = 'D:\\Users\\Ryan\\Google Drive CU\\Python\\Research-Tools\\Molecules\\PEROXIDE'
foldersLocation = 'D:\\Users\\Ryan\\Documents\\Scrap\\Folders'

# baseLocation = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\TiO2Surface\\CONTCAR'
# moleculeLocation = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\Molecules\\PEROXIDE'
# foldersLocation = 'D:\\Users\\theme\\Documents\\Scrap\\'
fileName = 'POSCAR'




i = 0
for a in aPts:
    for b in bPts:
        for c in cPts:
            for yaw in yaws:
                for pitch in pitchs:
                    for roll in rolls:

                        base = loadPosFile(baseLocation)
                        molecule = loadPosFile(moleculeLocation)
                        yaw = NP.longdouble(yaw)
                        pitch = NP.longdouble(pitch)
                        roll = NP.longdouble(roll)
                        location = NP.matrix([a,b,c])
                        saveLocation = os.path.join(foldersLocation, str(i), fileName)
                        try:
                            os.makedirs(os.path.join(foldersLocation, str(i)))
                        except:
                            print('Folder Already Exists, contents overwritten at' + saveLocation)
                        savePosfile(addAndRotate(base,molecule,location, roll, pitch, yaw), saveLocation)
                        i += 1