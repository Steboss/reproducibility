#!/bin/bash
#SBATCH -o somd-array-gpu-%A.%a.out
#SBATCH -p Tesla
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH --time 48:00:00
#SBATCH --array=0-15

module load cuda/7.0

export OPENMM_CUDA_COMPILER=/usr/local/cuda-7.0/bin/nvcc

echo "CUDA DEVICES:" $CUDA_VISIBLE_DEVICES

lamvals=( 0.0000 0.0109 0.0432 0.095 0.1654 0.2499 0.3454 0.4477 0.5522 0.6545 0.7499 0.8345 0.9045 0.9567 0.9890 1.0000)

lam=${lamvals[SLURM_ARRAY_TASK_ID]}

echo "lambda is: " $lam

mkdir lambda-$lam
cd lambda-$lam
cp ../../input/MORPH.pert . 
cp ../../input/sim.cfg . 
cp ../../input/SYSTEM.top .
cp ../../input/SYSTEM.crd .

#export OPENMM_PLUGIN_DIR=/home/julien/sire.app/lib/plugins/

srun /home/julien/sire.app/bin/somd-freenrg -C sim.cfg -l $lam -p CUDA
cd ..

wait

    bash water_analysis.sh


