__author__ = 'Ryan'
import math
import numpy as NP
import numpy.linalg as LA
import rotation


def addAndRotate(baseFile, toAdd, origin, roll, pitch, yaw):
    toAdd = rotatePoints(toAdd, vecToCart(baseFile["vectors"], origin), NP.longdouble(roll), NP.longdouble(pitch), NP.longdouble(yaw))
    #toAdd = translateToOrigin(toAdd)
    return combinePosFiles(baseFile, toAdd, origin)



def rotatePoints(posDict, origin, roll, pitch, yaw):
    newDict = posDict
    R = rotation.z(yaw) * rotation.y(pitch) * rotation.x(roll)
    for atom in posDict["labels"]:
        for i in range(len(posDict["atoms"][atom])):
            a = vecToCart(posDict["vectors"], posDict["atoms"][atom][i])
            final = (R*a.transpose()).transpose()
            newDict["atoms"][atom][i] = cartToVec(posDict["vectors"], final)
    return newDict

def translateToOrigin(posDict):
    newDict = posDict
    mina=1
    minb=1
    minc=1
    for label in posDict['labels']:
        for i in range(len(posDict['atoms'][label])):
            a = posDict['atoms'][label][i]
            mina = NP.mod(a[0,0],1) if NP.mod(a[0,0],1) < mina else mina
            minb = NP.mod(a[0,1],1) if NP.mod(a[0,1],1) < minb else minb
            minc = NP.mod(a[0,2],1) if NP.mod(a[0,2],1) < minc else minc
    for label in posDict['labels']:
        for i in range(len(posDict['atoms'][label])):
            a = posDict['atoms'][label][i]
            newDict['atoms'][label][i][0,0] = a[0,0] - mina
            newDict['atoms'][label][i][0,1] = a[0,1] - minb
            newDict['atoms'][label][i][0,2] = a[0,2] - minc
    return newDict

def combinePosFiles(baseFile, toAdd, point):
    newBase = baseFile
    for i in range(len(toAdd["labels"])):
        label = toAdd["labels"][i]
        count =  toAdd["count"][i]
        if label in baseFile["labels"]:
            j = baseFile["labels"].index(label)
            newBase["count"][j] += count
        else:
            newBase["labels"].append(label)
            newBase["count"].append(count)
            newBase["atoms"][label] = []
            newBase['movement'][label] = []
        for i in range(len(toAdd['atoms'][label])):
            coord = vecToVec(toAdd["vectors"],baseFile["vectors"],toAdd['atoms'][label][i]) + point
            newBase["atoms"][label].append(coord)
            newBase['movement'][label].append(toAdd['movement'][label][i])
    return newBase


def savePosfile(toSave, whereToSave):
    toWrite = toSave['title_true'] + toSave['scale_true'] + toSave['a_true'] + toSave['b_true'] + toSave['c_true'] + '    '
    for label in toSave['labels']:
        toWrite = toWrite + label + '   '
    toWrite = toWrite + '\n    '
    for atom in toSave['count']:
        toWrite = toWrite + str(atom) + '   '
    toWrite = toWrite + '\n'
    toWrite = toWrite + 'S\n' if toSave['selective_dynamics'] else toWrite
    toWrite = toWrite + toSave['input'] + '\n'
    for label in toSave['labels']:
        for i in range(len(toSave['atoms'][label])):
            coord = toSave['atoms'][label][i].tolist()[0]
            toWrite = toWrite + '    ' + ' '.join(map(lambda x: str(x.min()), coord))
            if toSave['selective_dynamics']:
                toWrite = toWrite + ' ' + ' '.join(toSave['movement'][label][i])
            toWrite = toWrite + '\n'

    with open(whereToSave, 'wb') as f:
        f.write(bytes(toWrite, 'UTF-8'))
    return


# takes a file with path specified by first (and only) argument
# file MUST be formatted with no extra newlines
def loadPosFile(toOpen):  # requires POSCAR with title and no comments along vectors or atoms
    with open(toOpen) as f:
        lines = f.readlines()
        i = 0
        posDict = {}
        posDict['title'] = lines[i].strip()  # setting title
        posDict['title_true'] = lines[i]
        i += 1
        posDict['scale'] = int(NP.longdouble(lines[i].split()[0]))  # setting the scale
        posDict['scale_true'] = lines[i]
        i += 1
        posDict['a'] = list(map(NP.longdouble, lines[i].split()[0:3]))  # setting the a vector
        posDict['a_true'] = lines[i]
        i += 1
        posDict['b'] = list(map(NP.longdouble, lines[i].split()[0:3]))  # setting the b vector
        posDict['b_true'] = lines[i]
        i += 1
        posDict['c'] = list(map(NP.longdouble, lines[i].split()[0:3]))  # setting the c vector
        posDict['c_true'] = lines[i]
        posDict['vectors'] = NP.matrix([posDict['a'], posDict['b'], posDict['c']])
        i += 1
        posDict['labels'] = lines[i].strip().split()
        posDict['labels_true'] = lines[i]
        i += 1
        posDict['count'] = list(map(int, lines[i].split()))
        posDict['count_true'] = lines[i]
        i += 1
        if lines[i].strip()[0].upper() == 'S':
            posDict['selective_dynamics'] = True
            i += 1
        else:
            posDict['selective_dynamics'] = False
        input = lines[i].strip()[0].upper()
        if input == 'D':
            posDict['input'] = 'D'
        elif input == 'C':
            posDict['input'] = 'C'
        else:
            raise Exception('Invalid coordinates, specify either D(irect) or C(artesian)')
        i += 1

        posDict['atoms'] = {}
        posDict['movement'] = {}
        for l in range(len(posDict['labels'])):
            label = posDict['labels'][l]
            posDict['atoms'][label] = []
            posDict['movement'][label] = []
            for i in range(i, i+posDict['count'][l]):
                posDict['atoms'][label].append(NP.matrix(list(map(NP.longdouble, lines[i].split()[0:3]))))
                if posDict['selective_dynamics']:
                    posDict['movement'][label].append(lines[i].split()[3:6])
                else:
                    posDict['movement'][label].append(['T', 'T', 'T'])
            i += 1
    return posDict

# Converts between vector coordinate systems from iv to fv
def vecToVec(iv, fv, pt):
    fv = NP.float64(fv)
    fp = pt * iv * NP.longdouble(LA.inv(fv))
    return fp

def vecToSph(vectors, point):
    return cartToSph(vecToCart(vectors, point))

def vecToCart(vectors, point):
    return point*vectors

def cartToSph(xyz):
    ptsnew = NP.zeros(xyz.shape)
    xy = xyz[:,0]**2 + xyz[:,1]**2
    ptsnew[:,0] = NP.sqrt(xy + xyz[:,2]**2)
    ptsnew[:,1] = NP.arctan2(xyz[:,1], xyz[:,0])
    ptsnew[:,2] = NP.arctan2(NP.sqrt(xy), xyz[:,2]) # for elevation angle defined from Z-axis down
    return ptsnew

def sphToCart(point):
    ptsnew = NP.zeros(point.shape)
    ptsnew[:,0] = point[:,0]*NP.sin(point[:,2])*NP.cos(point[:,1])
    ptsnew[:,1] = point[:,0]*NP.sin(point[:,2])*NP.sin(point[:,1])
    ptsnew[:,2] = point[:,0]*NP.cos(point[:,2])
    return ptsnew

def sphToVec(vectors, point):
    return cartToVec(vectors, sphToCart(point))

def cartToVec(vectors, point):
    return vecToVec(NP.matrix([[1,0,0],[0,1,0],[0,0,1]]), vectors, point)

def dot(vector1, vector2):
    return sum(p*q for p,q in zip(vector1, vector2))
