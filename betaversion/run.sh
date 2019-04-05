#!/bin/bash

#SBATCH --time=1:00:00  # time requested in hour:minute:second
#SBATCH --cpus-per-task=1
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4

module load AUGUSTUS/3.2.3-intel-2017.u2-Python-2.7.13
mpiexec -n 2 python process_json.py