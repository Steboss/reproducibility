#!/bin/bash


for f in */ ; do  
cd $f/cyclo/allbonds/output; 
rm somd-array-gpu-*; 
cp -r  ~/projects/reproducibility/diatomic_pert/logP/analysis_toolkit/*  . ; 
python move_alc.py; 
wait; 
cd analysis_gro; 
python alchemical_analysis.py -a 'Sire' -p 'lambda*' -q '' -d '.' -r '4' -m 'TI-CUBIC' -g;
wait; 
cd ../../../none/output; 
rm somd-array-gpu-*; 
cp -r ~/projects/reproducibility/diatomic_pert/logP/analysis_toolkit/* . ; 
python move_alc.py; 
wait; 
cd analysis_gro; 
python alchemical_analysis.py -a 'Sire' -p 'lambda*' -q '' -d '.' -r '4' -m 'TI-CUBIC' -g;
wait; 
cd ../../../../water/allbonds/output; 
rm somd-array-gpu-*; 
cp -r ~/projects/reproducibility/diatomic_pert/logP/analysis_toolkit/* . ; 
python move_alc.py; 
wait; 
cd analysis_gro; 
python alchemical_analysis.py -a 'Sire' -p 'lambda*' -q '' -d '.' -r '4' -m 'TI-CUBIC' -g;
wait; 
cd ../../../none/output; 
rm somd-array-gpu-*; 
cp -r ~/projects/reproducibility/diatomic_pert/logP/analysis_toolkit/* . ; 
python move_alc.py; 
wait; 
cd analysis_gro; 
python alchemical_analysis.py -a 'Sire' -p 'lambda*' -q '' -d '.' -r '4' -m 'TI-CUBIC' -g;
wait; 
cd ../../../../vacuum/allbonds/output; 
rm somd-array-gpu-*;
cp -r ~/projects/reproducibility/diatomic_pert/logP/analysis_toolkit/* . ; 
python move_alc.py; 
wait; 
cd analysis_gro; 
python alchemical_analysis.py -a 'Sire' -p 'lambda*' -q '' -d '.' -r '4' -m 'TI-CUBIC' -g;
wait; 
cd ../../../none/output; 
rm somd-array-gpu-*; 
cp -r ~/projects/reproducibility/diatomic_pert/logP/analysis_toolkit/* . ; 
python move_alc.py; 
wait; 
cd analysis_gro; 
python alchemical_analysis.py -a 'Sire' -p 'lambda*' -q '' -d '.' -r '4' -m 'TI-CUBIC' -g;
wait; 
cd ../../../../../; 
done

