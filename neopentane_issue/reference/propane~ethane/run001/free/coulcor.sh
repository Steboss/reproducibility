#!/bin/bash
#SBATCH -o somd-coulcor-%A.%a.out
#SBATCH -p serial
#SBATCH -n 1
#SBATCH --time 48:00:00

module load openmm/6.3

cd output
mv FUNC_0.py lambda-0.0000/.
cd lambda-0.0000
cp ../MORPH.pert .
cp ../sim.cfg .

srun /home/julien/sire.app/bin/python  FUNC_0.py 1> ../freenrg-COULCOR-0.0000.dat 2> /dev/null

wait
cd ..

mv FUNC_1.py lambda-1.0000/.
cd lambda-1.0000
cp ../MORPH.pert .
cp ../sim.cfg .
srun /home/julien/sire.app/bin/python FUNC_1.py 1> ../freenrg-COULCOR-1.0000.dat 2>/dev/null
wait
cd ..


# Extract final value
python parsecoul.py freenrg-COULCOR-0.0000.dat freenrg-COULCOR-1.0000.dat > freenrg-COULCOR.dat
wait
