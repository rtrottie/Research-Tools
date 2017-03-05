import random
import numpy as NP
import numpy.linalg as LA
from helpers import *


#region VectorConversionTest
print('\n\nTESTING VECTOR CONVERSION \n\n')

vector1 = NP.matrix([[random.random()*100, random.random()*100, random.random()*100],
           [random.random()*100, random.random()*100, random.random()*100],
           [random.random()*100, random.random()*100, random.random()*100]])
vector2 = NP.matrix([[random.random()*100, random.random()*100, random.random()*100],
           [random.random()*100, random.random()*100, random.random()*100],
           [random.random()*100, random.random()*100, random.random()*100]])
point = NP.matrix([random.random()*100, random.random()*100, random.random()*100])

print(vecToCart(vector1, point))
print(vecToCart(vector2, vecToVec(vector1, vector2, point)))
print(point)
print(vecToVec(vector2, vector1, vecToVec(vector1, vector2, point)))

#endregion

#region SphericalTest
print("\n\nTESTING SPHERICAL\n\n")
print(point)
print(sphToCart(cartToSph(point)))
print(cartToSph(point))
#endregion

#region cartToVec
print('\n\nTESTING CARTESIAN TO VECTOR')
print(point)
print(vecToCart(vector1, cartToVec(vector1, point)))
print(vecToCart(vector2, cartToVec(vector2, point)))
#endregion

#region SpinTest
print('\n\nTESTING ROTATION AND ORIGINING\n\n')
#fLoc = 'C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\TIO2_LARGE'
fLoc = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\Molecules\\DIMETHAMINE'
sLoc = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\TIO2_LARGE'
fLoc = sLoc
o = NP.matrix([1,1,1])
ref = NP.matrix([1,-20,-20])
o.tolist()
p= loadPosFile(fLoc)
r = rotatePoints(p,o,ref)
s = translateToOrigin(r)
savePosfile(s, sLoc)
#endregion

#region CombineTest
# bLoc = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\TiO2Surface\\CONTCAR'
# aLoc = sLoc
# point = NP.matrix([.5,0.8,.5])
# cLoc = 'D:\\My Stuff\\Dropbox\Dropbox\\Research\\PycharmProjects\\Scrap\\combined\\CONTCAR'
# a = loadPosFile(aLoc)
# b = loadPosFile(bLoc)
#
# c = combinePosFiles(b, a, point)
# savePosfile(c, cLoc)

#endregion


# p= loadPosFile('C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\TIO2_LARGE')
# savePosfile(p,'C:\\Users\\Ryan\\Dropbox\\Research\\PycharmProjects\\Scrap\\CONTCAR')