#!/bin/bash

# for the creation of this look at slide 7 of 6.2 remote computing for important bits of SLURM script
# for further guidance copy and paste prompt into chat gpt to display proper formatting
# not all aspects of SLURM script needed so adjust what the variables call and add additional lines

# Define variables for the SLURM script
job_name = "my_job"
queue = "batch"
num_nodes = 1
num_processors = 8
walltime = "00:01:00"

# Print the SLURM script to STDOUT
print("#!/bin/bash")
print("#SBATCH --job-name=" + job_name)
print("#SBATCH --partition=" + queue)
print("#SBATCH --nodes=" + str(num_nodes))
print("#SBATCH --ntasks-per-node=" + str(num_processors))
print("#SBATCH --time=" + walltime)
print("#SBATCH -o %j.out")
print("#SBATCH -e %j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=gjmcinto@uark.edu")

# Add any additional commands you want to run on the compute nodes here
print("echo 'Hopefully I did this right!'")
