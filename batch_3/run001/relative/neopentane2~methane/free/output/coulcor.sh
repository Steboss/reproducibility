#!/bin/bash
#SBATCH -o somd-coulcor-%A.%a.out
#SBATCH -p serial
#SBATCH -n 1
#SBATCH --time 48:00:00

module load openmm/6.3

cp FUNC.py  lambda-0.0000/.

cd lambda-0.0000
srun ~/sire.app/bin/python  FUNC.py 1> ../freenrg-COULCOR.dat 2> /dev/null
cd ..
wait

# Extract final value
