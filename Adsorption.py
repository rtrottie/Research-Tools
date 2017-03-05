import pymatgen as pmg
import numpy as np
import os
import os.path as path
import pymatgen.transformations.standard_transformations as std_trns
import pymatgen.transformations.site_transformations as site_trns
import pymatgen.core.operations as oprs


def align_molecule(molecule, aligned_axis, aligned_atom, centered_atom, spin=0, angle_in_radians=False):
    """
    Aligns provided molecule so the provided atom (or default: center of mass) lies along the specified axis from the
    origin at centered_atom

    Args:
        :type molecule: pmg.core.Molecule
        :type aligned_axis: np.matrix
        :type aligned_atom: int | None
        :type centered_atom: int | None
        :rtype: pmg.core.Molecule
        :return:
    """
    if centered_atom == None:
        translation_vector = -molecule.center_of_mass
    else:
        translation_vector = -molecule.sites[centered_atom].coords

    translation_operation = oprs.SymmOp.from_axis_angle_and_translation([1, 0, 0], 0, True, translation_vector)
    molecule.apply_operation(translation_operation)

    if aligned_atom == None:
        unaligned_axis = molecule.center_of_mass
    else:
        unaligned_axis = molecule.sites[aligned_atom].coords
    rotation_axis = np.cross(unaligned_axis, aligned_axis)
    rotation_angle = np.arccos(np.dot(unaligned_axis,aligned_axis)/(np.linalg.norm(unaligned_axis)*np.linalg.norm(aligned_axis)))
    rotation_operation = oprs.SymmOp.from_axis_angle_and_translation(rotation_axis, rotation_angle, True)
    molecule.apply_operation(rotation_operation)

    spin_operation = oprs.SymmOp.from_axis_angle_and_translation(aligned_axis, spin, angle_in_radians)
    molecule.apply_operation(spin_operation)