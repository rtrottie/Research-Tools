import pymatgen as pmg
import numpy as np
import os
import os.path as path
import pymatgen.transformations.standard_transformations as trns
import Adsorption
import Vis

VESTA_DIR = '/home/ryan/programs/vesta/VESTA-x86_64/VESTA '
MOLECULE_DIR = '/home/ryan/PycharmProjects/Research-Tools/Molecules'
MOLECULE = 'TMA.gjf'
SCRATCH = '/home/ryan/scratch'
#
# aligned_atom = 0
# aligned_axis = np.array([0,0,1])



molecule = pmg.core.structure.Molecule.from_file(path.join(MOLECULE_DIR,MOLECULE))
print(molecule)

aligned_molecule = Adsorption.align_molecule(molecule, [0,0,1], None, 0, 30)
print(molecule)

# Vis.open_in_VESTA(centered_molecule)
# Vis.open_in_VESTA(molecule)
