from pymatgen.core.structure import Structure

crystal = Structure.from_file("/home/pinyang_umass_edu/cgcnn/IZASC_re/ATN-0.cif")
for i, site in enumerate(crystal):
    print(site.is_ordered)

print(crystal.composition.reduced_formula == 'SiO2')