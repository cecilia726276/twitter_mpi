#!/bin/bash
#SBATCH --ntasks-per-node=8
#SBATCH --nodes=1
#SBATCH --time=0-00:10:00
#SBATCH --partition=cloud

module load AUGUSTUS/3.2.3-intel-2017.u2-Python-2.7.13
time mpiexec -n 8 python process_json.py