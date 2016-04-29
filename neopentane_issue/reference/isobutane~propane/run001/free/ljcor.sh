#!/bin/bash
#SBATCH -o somd-ljcor-%A.%a.out
#SBATCH -p serial
#SBATCH -n 1
#SBATCH --time 48:00:00

cd output

cd lambda-0.0000

srun /home/julien/sire.app/bin/somd-lj-tailcorrection -C ../../input/sim.cfg -l 0.00 -b "1.00 * gram / (centimeter*centimeter*centimeter)" -r traj000000001.dcd -s 20 1> ../freenrg-LJCOR-lam-0.0000.dat 2> /dev/null

wait

cd ..


cd lambda-1.0000

srun /home/julien/sire.app/bin/somd-lj-tailcorrection -C ../../input/sim.cfg -l 1.00 -b "1.00 * gram / (centimeter*centimeter*centimeter)" -r traj000000001.dcd -s 20 1> ../freenrg-LJCOR-lam-1.0000.dat 2> /dev/null

wait
cd ..


# utility script to get final LJ correction term
python parselj.py freenrg-LJCOR-lam-0.0000.dat freenrg-LJCOR-lam-1.0000.dat > freenrg-LJCOR.dat
