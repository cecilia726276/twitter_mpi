#!/bin/sh
#SBATCH -N 1      # nodes requested
#SBATCH -n 1      # tasks requested
#SBATCH -c 4      # cores requested
#SBATCH --mem=500  # memory in Mb
#SBATCH -o outfile  # send stdout to outfile
#SBATCH -e errfile  # send stderr to errfile
#SBATCH -t 0:01:00  # time requested in hour:minute:second

module load AUGUSTUS/3.2.3-intel-2017.u2-Python-2.7.13
mpiexec -np 4 python readtiny_test.py