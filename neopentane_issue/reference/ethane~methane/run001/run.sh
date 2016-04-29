#!/bin/bash


cd vacuum/output
sbatch ../vacuum.sh
cd ../../free/output
sbatch ../water.sh

