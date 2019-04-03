#!/bin/bash#
#SBATCH -N 1      # nodes requested
#SBATCH -n 8      # cores requested
#SBATCH -o outfile  # send stdout to outfile
#SBATCH -e errfile  # send stderr to errfile

module load AUGUSTUS/3.2.3-intel-2017.u2-Python-2.7.13
mpiexec -np 8 python process_json.py