#! /usr/bin/env python3

#import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script opens and reads a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help="The gff file to be read", type=str)
parser.add_argument("fasta", help="The fasta file to be read", type=str)

# parse the actual argument
args = parser.parse_args()

with open(args.gff, "r") as gff_file:
    for line in gff_file:
        print(line.strip())

with open(args.fasta, "r") as fasta_file:
    for line in fasta_file:
        print(line.strip())
