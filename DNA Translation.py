# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:44:55 2016

@author: AB Sanyal

A DNA will consist of codons of length 3, made of the nitrogenous bases 0 and 1.
Each codon corresponds to an amino acid, which makes the full protein.

"""

import random
import numpy as np

#testing

#Declaration of certain constants
codon_length = 3   #Length of a codon
mutation_rate = 0.1   #Rate of mutation out of 1

#Dictionary of amino-acids
amino_acid = dict([("000", 0),
                   ("001", 1),
                    ("010", 2),
                    ("011", 3),
                    ("100", 4),
                    ("101", 5),
                    ("110", 6),
                    ("111", 7)])

#Generate a random DNA, which is a sequence of 0's and 1's. The length should be a multiple of 3 in this case (but not necessarily).
def create_random_dna(length):
    i = 1
    dna = []
    while (i <= length):
        dna.append(random.randint(0, 1))
        i += 1
    return dna

#Show a formatted sequence where elements are separated by '-'
def show_seq(seq, separator):
    i = 0
    p = ""
    while (i < len(seq)):
        p += str(seq[i])
        if (i < len(seq) - 1):
            p += str(separator)
        i += 1
    return p

#Format DNA into codons
def show_DNA_seq(seq):
    i = 0
    p = ""
    while (i < len(seq)):
        p += str(seq[i])
        if (i < len(seq) - 1 and (i + 1) % codon_length == 0):
            p += "-"
        i += 1
    return p

#Translate each three base block (codon) into an amino acid and form a sequence of amino acids
def translate(dna_original):
    dna = dna_original[:]
    #Trim the DNA so that excess parts are gone in case the number of bases is not a multiple of codon_length
    excess_bases = len(dna) % codon_length
    i = 1
    while (i <= excess_bases):
        dna.pop()
        i += 1
    #Scan the DNA
    i = 0
    protein = []
    while (i < len(dna)):
        #Scan eaach codon and translate to an amino-acid
        j = i
        codon = ""
        while (j < i + codon_length):
            codon += str(dna[j])
            j += 1
        protein.append(amino_acid[codon])
        i += 3
    return protein

#Random rubstitution mutation
def substitute_random(dna_original):
    dna = dna_original[:]
    i = 0
    while (i < len(dna)):
        if (np.random.uniform(0, 1) < mutation_rate):
            if (dna[i] == 0):
                dna[i] = 1
            else:
                if (dna[i] == 1):
                    dna[i] = 0
        i += 1
    return dna

#Function to test similarity between two DNA strands
def fitness(s, target):
    i = 0
    k = 0
    while(i < len(s)):
        k += abs(target[i] - s[i])
        i += 1
    #k = np.sqrt(k)
    return k

def changed_positions(s1, s2):
    positions = []
    if (len(s1) <= len(s2)):
        i = 0
        while (i < len(s1)):
            if (s1[i] != s2[i]):
                positions.append(i)
            i += 1
    else:
        i = 0
        while (i < len(s2)):
            if (s1[i] != s2[i]):
                positions.append(i)
            i += 1
    return positions

#Run tests
sample_dna = create_random_dna(1000)
print("\nThe DNA is:")
print(show_DNA_seq(sample_dna))
print("\nThe translated protein is:")
protein = translate(sample_dna)
print(show_seq(protein, "-"))
print("\nThe mutated DNA is:")
mutated_dna = substitute_random(sample_dna)
print(show_DNA_seq(mutated_dna))
print("\nThe mutated protein is:")
protein = translate(mutated_dna)
print(show_seq(protein, "-"))
print("\nNumber of changes:")
print(fitness(mutated_dna, sample_dna))
print("\nChanges in the DNA occured at positions:")
print(show_seq(changed_positions(sample_dna, mutated_dna), ", ") + ".")
