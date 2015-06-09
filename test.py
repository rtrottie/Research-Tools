import pymatgen as pmg
import numpy as np
import os
import os.path as path
import pymatgen.transformations.standard_transformations as trns

VESTA_DIR = '/home/ryan/programs/vesta/VESTA-x86_64/VESTA '
MOLECULE_DIR = '/home/ryan/PycharmProjects/Research-Tools/Molecules'
MOLECULE = 'TMA.gjf'
SCRATCH = '/home/ryan/scratch'

aligned_atom = 0
aligned_axis = np.array([0,0,1])

molecule = pmg.core.structure.Molecule.from_file(path.join(MOLECULE_DIR,MOLECULE)).get_centered_molecule()

molecule.to('xyz',path.join(SCRATCH,'scratch.xyz'))

unaligned_axis = molecule.sites[aligned_atom].coords
rotation_axis = np.cross(unaligned_axis, aligned_axis)
rotation_axis = rotation_axis/np.linalg.norm(rotation_axis)
rotation_angle = np.arccos(np.dot(unaligned_axis,aligned_axis)/(np.linalg.norm(unaligned_axis)*np.linalg.norm(aligned_axis)))*180/np.pi


rotation_transformation = trns.RotationTransformation(rotation_axis,rotation_angle)
atom_list = molecule.sites
periodic_list = list(map(lambda site: pmg.core.sites.PeriodicSite(site.specie.number,
                                                                  site.coords,
                                                                  pmg.core.Lattice(np.matrix([[20,0,0],[0,20,0],[0,0,20]])),
                                                                  coords_are_cartesian=True),
                         atom_list))

molecule_periodic = pmg.core.Structure.from_sites(periodic_list)

molecule_rotated = rotation_transformation.apply_transformation(molecule_periodic)

print(rotation_transformation)

print('## INITIAL ##')
print(molecule.cart_coords)
print('## PERIODIC ##')
print(molecule_periodic.cart_coords)
print('## ROTATED ##')
print(molecule_rotated.cart_coords)

print(rotation_angle)
print(rotation_axis)
