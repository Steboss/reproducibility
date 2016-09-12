#!/bin/bash
#SBATCH -o analyse-free-nrg-%A.%a.out
#SBATCH -p serial
#SBATCH -n 1
#SBATCH --time 00:05:00
#SBATCH --array 0

echo "Task ID" $SLURM_ARRAY_TASK_ID
srun /home/julien/sire.app/bin/analyse_freenrg_mbar -i lambda-0.0000/simfile.dat lambda-0.0625/simfile.dat lambda-0.1250/simfile.dat lambda-0.1875/simfile.dat lambda-0.2500/simfile.dat lambda-0.3125/simfile.dat lambda-0.3750/simfile.dat lambda-0.4375/simfile.dat lambda-0.5000/simfile.dat lambda-0.5625/simfile.dat lambda-0.6250/simfile.dat lambda-0.6875/simfile.dat lambda-0.7500/simfile.dat lambda-0.8125/simfile.dat lambda-0.8750/simfile.dat lambda-0.9375/simfile.dat lambda-1.0000/simfile.dat --lam 0.0000 0.0625 0.1250 0.1875 0.2500 0.3125 0.3750 0.4375 0.5000 0.5625 0.6250 0.6875 0.7500 0.8125 0.8750 0.9375 1.0000 --temperature 298.0 -o mbar.pmf --subsampling percentage --percentage 82 > freenrg-MBAR.dat

if [ "$SLURM_ARRAY_TASK_ID" -eq "0" ]
then
    #remember to find out how to export python modules from my home
    sleep 60
    echo "Task ID" $SLURM_ARRAY_TASK_ID
    python analysis_tot.py
fi

