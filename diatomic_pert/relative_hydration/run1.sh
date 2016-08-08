#!/bin/bash

python prepare.py  inputfiles/HC~HH/diff_masses/   inputfiles/HH~HC/diff_masses/
wait

cd run001/diff_masses/all_bonds/HC~HH/free/output
sbatch water.sh

cd ../../vacuum/output
sbatch vacuum.sh

cd ../../../HH~HC/free/output
sbatch water.sh

cd ../../vacuum/output
sbatch vacuum.sh



