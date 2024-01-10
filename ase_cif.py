import os
from ase.io import read, write

# Define input and output directories
input_dir = '/home/pinyang_umass_edu/cgcnn/IZASC/'  # Path to the folder containing the input CIF files
output_dir = '/home/pinyang_umass_edu/cgcnn/IZASC_c/'  # Path to the folder where the modified CIF files will be saved

# List all CIF files in the input directory
cif_files = [f for f in os.listdir(input_dir) if f.endswith('.cif')]

# Loop over each CIF file
for cif_file in cif_files:
    # Read the CIF file
    print(cif_file)
    cif_path = os.path.join(input_dir, cif_file)
    atoms = read(cif_path)
    output_path = os.path.join(output_dir, cif_file)
    write(output_path, atoms)