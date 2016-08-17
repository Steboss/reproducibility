#!/bin/bash

python prepare.py  inputfiles/HC/   inputfiles/HH/
wait

cd run001/diff_masses/all_bonds/HC/free/vanish/output
sbatch water.sh

cd ../../../../HH/free/vanish/output
sbatch water.sh

