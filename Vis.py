__author__ = 'ryan'
import os

def open_in_VESTA(molecule):
    VESTA_DIR = '/home/ryan/programs/vesta/VESTA-x86_64/VESTA '
    MOLECULE_DIR = '/home/ryan/PycharmProjects/Research-Tools/Molecules'
    MOLECULE = 'TMA.gjf'
    SCRATCH = '/home/ryan/scratch/scratch.xyz'

    molecule.to('xyz', SCRATCH)
    os.system(VESTA_DIR+SCRATCH)