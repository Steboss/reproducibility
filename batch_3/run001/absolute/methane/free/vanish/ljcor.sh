#!/bin/bash
#SBATCH -o somd-ljcor-%A.%a.out
#SBATCH -p serial
#SBATCH -n 1
#SBATCH --time 48:00:00

export PATH=/home/julien/sire.app/bin:$PATH

cd lambda-0.0000
srun ~/sire.app/bin/somd-lj-tailcorrection -C sim.cfg -l 0.00 -b "1.00 * gram / (centimeter*centimeter*centimeter)" -r traj000000001.dcd -s 20 1> ../freenrg-LJCOR-lam-0.000.dat 2> /dev/null

wait

cd ..
cd lambda-1.0000
srun ~/sire.app/bin/somd-lj-tailcorrection -C sim.cfg -l 1.00 -b "1.00 * gram / (centimeter*centimeter*centimeter)" -r traj000000001.dcd -s 20 1> ../freenrg-LJCOR-lam-1.000.dat 2> /dev/null
cd ..

wait

# utility script to get final LJ correction term
#/home/julien/local/bin/parselj.py freenrg-LJCOR-lam-0.000.dat freenrg-LJCOR-lam-1.000.dat > freenrg-LJCOR.dat
