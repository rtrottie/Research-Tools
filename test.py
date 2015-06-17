import pymatgen as pmg
import numpy as np
import os
import os.path as path
import pymatgen.transformations.standard_transformations as trns
import pymatgen.io.vaspio as vasp
import Adsorption
import Vis


os.environ["VASP_PSP_DIR"]='/home/ryan/pseudopotential'
MOLECULE_DIR = '/home/ryan/PycharmProjects/Research-Tools/Molecules'
MOLECULE = 'TMA.gjf'
SURFACE_DIR = '/home/ryan/PycharmProjects/Research-Tools/Surfaces'
SURFACE = 'TiO2/POSCAR_TiO2_Large'
FOLDER = '/home/ryan/scratch/'


adsorbed_locations_fractional = [('O_Parallel', [0.49814, -0.03, 0.49103]), ('Ti', [0.67968, -0.03, 0.53606]), ('O_Perp', [0.40936, -0.06, 0.22763]), ('Vacuum', [.5,.75,.5])]
adsorbed_locations_fractional = [adsorbed_locations_fractional[3]]
rotations = [0, 40, 80]
rotations = [rotations[2]]
kpoints = vasp.Kpoints()
incar = vasp.Incar.from_file(os.path.join(FOLDER, 'INCAR'))

for (folder, adsorbed_location_fractional) in adsorbed_locations_fractional:
    for rotation in rotations:


        molecule = pmg.core.Molecule.from_file(path.join(MOLECULE_DIR,MOLECULE))
        Adsorption.align_molecule(molecule, [0, -1, 0.5], None, 0, rotation)

        surface_poscar = vasp.Poscar.from_file(path.join(SURFACE_DIR, SURFACE))
        surface = surface_poscar.structure.copy()

        for site in molecule.sites:
            adsorbed_location_cartesian = surface.lattice.get_cartesian_coords(adsorbed_location_fractional)
            surface.append(site.specie, adsorbed_location_cartesian + site.coords,True)
        surface.sort()
        poscar = vasp.Poscar(surface)
        potcar = vasp.Potcar(poscar.site_symbols)
        vasp.VaspInput(incar,kpoints,poscar,potcar).write_input(os.path.join(FOLDER,folder,str(rotation)))
        Vis.open_in_Jmol(surface,'cif')
        with open(os.path.join(FOLDER,folder,str(rotation),'TMA_'+folder+'_'+str(rotation)+'.log'),'w') as f:
            f.write('')