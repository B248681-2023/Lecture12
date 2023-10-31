#!/usr/bin/python3

import os
import subprocess
import shutil
import glob

sequence_directory = "/localdisk/data/BPSM/Lecture12/"

# Copy the files:
sequence_files = glob.glob(sequence_directory + "*")
for sequence_file in sequence_files:
    shutil.copy(sequence_file, ".")
shutil.copy(f"{sequence_directory}input.txt", ".")

# Read each line of the input.txt to get each sequence
# Trim off the first 14 characters
# Add trimmed sequences to a variable, one line at a time
# Print the length of each trimmed sequence
seqz = "./input.txt"
trimmed_seqs = ""
with open(seqz) as seq:
    for lyne in seq:
        if trimmed_seqs == "":
            trimmed_seqs = lyne[14:]
        else:
            trimmed_seqs += lyne[14:]
        print("Length of each sequence is "+ str(len(lyne[14:])))

# Write the trimmed sequences to a new file
with open(seqz, "w") as floop:
    floop.write(trimmed_seqs)

gen_sec_file = "/localdisk/data/BPSM/Lecture12/genomic_dna2.txt"
exons_file = "/localdisk/data/BPSM/Lecture12/exons.txt"

exon_start_stops = []
with open(exons_file) as exons:
    for exon in exons:
        if exon != "":
            print(exon)
            exon_start_stops.append(exon.rstrip().split(","))

with open(gen_sec_file) as genome:
    genome_contents = genome.read()
    exons_together = ""
    for start_stop in exon_start_stops:
#        exons_together += genome_contents[start_stop[0]-1:start_stop[1]]
        exons_together += genome_contents[int(start_stop[0])-1:int(start_stop[1])]

with open("coded_regions.txt", "w") as coded:
    coded.write(exons_together)

my_home = os.environ['HOME']
sliding_windowz=[]
with open(f"{my_home}/Exercises/Lecture11/AJ223353_coding_region.txt") as aj_seq:
    the_actgs = aj_seq.read()
    number_of_windows=int(len(the_actgs)/3)
    for i in range(number_of_windows):
        current_index = i*3
        sliding_window = the_actgs[current_index:current_index+30]
        print(sliding_window)
        print("The GC content is " + str(sliding_window.upper().count("C")/sliding_window.upper().count("G")))
        sliding_windowz.append(sliding_window)

# Remove existing windows fasta file if exists
try:
    os.path.exist("AJ223353_windows.fasta")
except:
    print("No existing fasta file to remove")
else:
    os.remove("AJ223353_windows.fasta")

# Loop through the windows (number of loops determined earlier) and append to fasta file
for j in range(number_of_windows):
    with open(f"AJ223353_windows.fasta", "a") as le_window:
        if j == 0:
            le_window.write(f"> Sliding window {i}\n{sliding_windowz[j]}")
        else:
            le_window.write(f"\n\n> Sliding window {i}\n{sliding_windowz[j]}")



