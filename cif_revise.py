import os
from pymatgen.core.structure import Structure
from pymatgen.io.cif import CifWriter

def cif_revise(cif_path, save_path):
    """
    Revise the cif file to make it readable by pymatgen.
    """
    cif_files = [f for f in os.listdir(cif_path) if f.endswith('.cif')]

    for cif_file in cif_files:
        input_path = os.path.join(cif_path, cif_file)
        crystal = Structure.from_file(input_path)
        # Change all occupancies to 1
        for i, site in enumerate(crystal):
            if (not site.is_ordered) or (not 'Si' in site.species_string):
                if 'O' in site.species_string:
                    crystal[i] = {'O': 1.0}
                else:
                    crystal[i] = {'Si': 1.0}

        # Delete duplicate sites
        crystal.merge_sites(tol=0.01, mode='delete')
        if crystal.composition.reduced_formula != 'SiO2':
            print(cif_file)
        # Write the structure to a cif file
        CifWriter(crystal).write_file(os.path.join(save_path, cif_file))

if __name__ == '__main__':
    cif_path = '/home/pinyang_umass_edu/cgcnn/IZASC/'
    save_path = '/home/pinyang_umass_edu/cgcnn/IZASC_re/'
    cif_revise(cif_path, save_path)