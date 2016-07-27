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

lamvals=( 0.0000 0.0544 0.0954 0.1464  0.2061 0.3454 0.5 0.6545 0.7269 0.7938 0.9085 0.9455 0.9755 0.9938 1.0000)

lam=${lamvals[SLURM_ARRAY_TASK_ID]}

echo "lambda is: " $lam

mkdir lambda-$lam
cd lambda-$lam
cp ../../input/sim.cfg . 
cp ../../input/SYSTEM.top . 
cp ../../input/SYSTEM.crd . 
cp ../../input/MORPH.pert . 

export OPENMM_PLUGIN_DIR=/home/julien/sire.app/lib/plugins/
export OPENMM_CPU_THREADS=1

srun /home/julien/sire.app/bin/somd-freenrg -C sim.cfg -l $lam -p CUDA
cd ..


