__author__ = 'Ryan'
import numpy as NP
from numpy import cos
from numpy import sin

def x(th):
    return NP.matrix([
        [1, 0, 0],
        [0, cos(th), -sin(th)],
        [0, sin(th), cos(th)]
    ])

def y(th):
    return NP.matrix([
        [cos(th), 0, sin(th)],
        [0, 1, 0],
        [-sin(th), 0, cos(th)]
    ])

def z(th):
    return NP.matrix([
        [cos(th), -sin(th), 0],
        [sin(th), cos(th), 0],
        [0, 0, 1]
    ])