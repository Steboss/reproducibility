#!/bin/bash

#APR 2015: bash script to launch atuomatically all the simulation
for f in *~* ; do 
 cd $f/run001/
 bash run.sh
# cd ../run002
# bash run.sh
 cd ../../
 done

