__author__ = 'Ryan'
from math import pi
import random
import os
from helpers import *


aPts = [0.34508]
bPts = [0.95, 1]
cPts = [0.532]

yaws = [0]
pitchs = [0, pi/2]
rolls = [0]



baseLocation = 'C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\TiO2Surface\\CONTCAR'
moleculeLocation = 'C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\Molecules\\ACETYLENE'
foldersLocation = 'C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\Folders'

# baseLocation = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\TiO2Surface\\CONTCAR'
# moleculeLocation = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\Molecules\\BENZENE'
# foldersLocation = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\Folders'
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