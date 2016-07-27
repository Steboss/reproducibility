#!/bin/bash


    #make sure to use my python/import sys sys.path.append("/home/steboss/.local")
    #TI esxtraction with regression scheme
    /home/julien/sire.app/bin/analyse_freenrg -g lambda-*/gradients.s3  >  freenrg-TI.dat
    wait
    #create analysisgro files to be analysed
    python analysis_alchemical.py
    wait
    cd analysis_gro
    #extract free energy change
    python alchemical_analysis.py -a 'Sire' -p 'lambda*' -q '' -d '.' -r '4' -m 'TI-CUBIC' -g
    wait
    cd ../
    python extract_results.py
    wait
    #create pdf 
    python grad_profile.py
    wait

