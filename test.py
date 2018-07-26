import pymatgen as pmg
import numpy as np
import os
import os.path as path
import pymatgen.transformations.standard_transformations as trns
import pymatgen.io.vasp as vasp
import Adsorption
import Vis

MOLECULE_DIR = 'D:\\Users\\RyanTrottier\\PycharmProjects\\Research-Tools\\Molecules'
MOLECULE = 'TMA_nonconv.xyz'
SURFACE_DIR = 'D:\\Users\\RyanTrottier\\PycharmProjects\\Research-Tools\\Surfaces'
SURFACE = 'TiO2/POSCAR_TiO2_Large'
FOLDER = 'D:\\Users\\RyanTrottier\\Documents\\Scrap'


adsorbed_locations_fractional = [('O_Parallel', [0.49814, -0.03, 0.49103]), ('Ti', [0.67968, -0.03, 0.53606]), ('O_Perp', [0.40936, -0.06, 0.22763]), ('Vacuum', [.5,.75,.5])] # can do multiple
# adsorbed_locations_fractional = [adsorbed_locations_fractional[3]]
axis_to_align_to = [0, 1, 0] # Will align the molecule (either by two specified atoms, or atom and center of mass)
rotations = [0, 40, 80] # how to spin the adsorbed moleulce w.r.t the provided axis
centered_atom  = 0 # atom that will be placed at given coordinates in adsorbed_locations_fractional
aligned_atom = 1 # atom that will be aligned along give axis with the centered atom.  If None, uses the center of mass
# rotations = [rotations[2]]
# kpoints = vasp.Kpoints()
# incar = vasp.Incar.from_file(os.path.join(FOLDER, 'INCAR'))

for (folder, adsorbed_location_fractional) in adsorbed_locations_fractional:
    for rotation in rotations:


        molecule = pmg.core.Molecule.from_file(path.join(MOLECULE_DIR,MOLECULE))
        Adsorption.align_molecule(molecule, axis_to_align_to , aligned_atom, centered_atom, rotation)

        surface_poscar = vasp.Poscar.from_file(path.join(SURFACE_DIR, SURFACE))
        surface = surface_poscar.structure.copy() # Structure

        for site in molecule.sites:
            adsorbed_location_cartesian = surface.lattice.get_cartesian_coords(adsorbed_location_fractional)
            surface.append(site.specie, adsorbed_location_cartesian + site.coords,True,properties={'selective_dynamics' : [True,True,True]})
        surface.sort()
        # poscar = vasp.Poscar(surface)
        # potcar = vasp.Potcar(poscar.site_symbols)
        # vasp.VaspInput(incar,kpoints,poscar,potcar).write_input(os.path.join(FOLDER,folder,str(rotation)))
        # Vis.open_in_Jmol(surface,'cif')
        os.makedirs(os.path.join(FOLDER, folder, str(rotation)),exist_ok=True)
        surface.to('poscar', os.path.join(FOLDER,folder,str(rotation),'TMA_'+folder+'_'+str(rotation)+'.vasp'))