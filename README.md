# Gaussian beam discrete dipole approximation
The following code is Draine's DDA version 7.3.2 edited to contain a Gaussian beam excitation source.

## Set up
Compile the code in the folder `source_code` by typing `make all`.

## Examples
The folder `example_sphere` contains example scripts to run a calculation of the light scattered by a nanosphere.
* Step 1: Create input files.
The file `make_sphere.py` will create a shape file of a nanosphere. To make the shape file, run `python make_sphere.py -w -l <lattice spacing> -r <radius in nm>`. This will create the file `shape.dat` which will be compatible with DDSCAT. To verify your shape, you can plot the shape via `python make_sphere.py -p` which will plot the shape file.
* Step 2: Create parameter files.
Edit the file `ddscat.par` according to the normal methods defined in Draine's User Guide. The only modifications are to lines 28 - 31, which specify the Gaussian beam parameters.
* Step 3: Run the script.
To run the script, type `bash run_gdda.sh`. For a 5 nm radius sphere of 1 nm dipole spacing, the code should run within seconds on a local computer. 