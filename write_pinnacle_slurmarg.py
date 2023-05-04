#!/usr/bin/env python3

import argparse

# Define default variables for the SLURM script
DEFAULT_JOB_NAME = "my_job"
DEFAULT_QUEUE = "comp01"
DEFAULT_NUM_NODES = 1
DEFAULT_NUM_PROCESSORS = 24
DEFAULT_WALLTIME = 1

# Set up argparse to parse command-line arguments
parser = argparse.ArgumentParser(description="Generate a SLURM script with customizable options")
parser.add_argument("job_name", nargs="?", default=DEFAULT_JOB_NAME,
                    help="name of the job")
parser.add_argument("-q", "--queue", default=DEFAULT_QUEUE,
                    help="name of the queue")
parser.add_argument("-n", "--num-nodes", type=int, default=DEFAULT_NUM_NODES,
                    help="number of nodes")
parser.add_argument("-p", "--num-processors", type=int, default=DEFAULT_NUM_PROCESSORS,
                    help="number of processors per node")
parser.add_argument("-t", "--walltime", default=DEFAULT_WALLTIME,
                    help="walltime for the job")

args = parser.parse_args()

# Get the values of the variables from the command-line arguments or defaults
job_name = args.job_name
queue = args.queue
num_nodes = args.num_nodes
num_processors = args.num_processors
walltime = args.walltime

# Print the SLURM script to STDOUT
print("#!/bin/bash")
print("#SBATCH --job-name=" + job_name)
print("#SBATCH --partition=" + queue)
print("#SBATCH --nodes=" + str(num_nodes))
print("#SBATCH --ntasks-per-node=" + str(num_processors))
print("#SBATCH --time=" + str(walltime) + ':00:00')
print("#SBATCH -o %j.out")
print("#SBATCH -e %j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=gjmcinto@uark.edu")

# Add any additional commands you want to run on the compute nodes here
print("echo 'Hopefully I did this right'")
