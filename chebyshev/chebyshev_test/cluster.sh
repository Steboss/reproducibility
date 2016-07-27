#!/bin/bash

#APR 2015: bash script to launch atuomatically all the simulation

for f in *_masses/*/*/*/vacuum ; do

homefold=$(pwd)

cd $f/output/

sbatch ../vacuum.sh

cd $homefold

done

for f in *_masses/*/*/*/free/ ; do 
homefold=$(pwd)
cd $f/output/

sbatch ../water.sh

cd $homefold
done
