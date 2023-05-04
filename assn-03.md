1. rsync -rv mt_genomes/ gjmcinto@hpc-portal2.hpc.uark.edu:/storage/gjmcinto  
2. scp -v unkonwn.fa gjmcinto@hpc-portal2.uark.edu:/storage/gjmcinto  
3. nano job.slurm  
  
#!/bin/bash  

#SBATCH --job-name+assn03  
#SBATCH --partition comp01  
#SBATCH --nodes=1  
#SBATCH --qos comp  
#SBATCH --tasks-per-node=1  
#SBATCH --time=00:01:00  
#SBATCH -o test_%j.out  
#SBATCH -e test_%j.err  
#SBATCH --mail-type=ALL  
#SBATCH --mail-user=gjmcinto@uark.edu  
  
#export OMP_NUM_THREADS=32  
  
module purge  
module load blast/2.3.0+  
  
cd $SLURM_SUBMIT_DIR  
# job command here  
  
#concatonate fasta files  
cat *.fasta > genomes.fas  
  
#make the blast database  
maskeblastdb -in genomes.fas -dbtype nucl  
  
blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn  
  
cntrl 0, enter, cntrl x  
  
sbatch job.slurm  
4. rync -ur gjmcinto@hpx-portal2.hpc.uark.edu :/storage/gjmcinto/mt_genomes /mnt/c/Users/mack/Desktop/watermelon_files  
5. run time = 0.231557 seconds  
Cucurbita had highest score so closest match  

