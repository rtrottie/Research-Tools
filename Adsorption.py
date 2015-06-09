import pymatgen as pmg
import numpy as np
import os
import os.path as path
import pymatgen.transformations.standard_transformations as trns

def align_molecule(molecule, aligned_axis, aligned_atom=None):
    """
    Aligns provided molecule so the provided atom lies along the specified axis

    Args:
        :type molecule: pmg.core.structure.Molecule
        :type aligned_axis: np.matrix
        :type aligned_atom: int
    """
    if aligned_atom == None:
        unaligned_axis = molecule.center_of_mass
    else:
        unaligned_axis = molecule.sites[aligned_atom].coords
    molecule.