#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, ".."))
from ORF import orf
from optparse import OptionParser
from Bio import SeqIO


def extract_feature_from_seq(seq, stt, stp):
    stt_coden = stt.strip().split(',')
    stp_coden = stp.strip().split(',')
    mRNA_seq = seq.upper()
    mRNA_size = len(seq)
    tmp = orf.ORFFinder(mRNA_seq)
    (CDS_size, CDS_frame, CDS_seq) = tmp.longest_orf(direction="+", start_coden=stt_coden, stop_coden=stp_coden)
    coverage = float(CDS_size) / mRNA_size
    return coverage

def main():
    usage = "\n%prog [options]"
    parser = OptionParser(usage,version="%prog ")
    parser.add_option("-i","--input",action="store",dest="input_file",help="mRNA sequences in FASTA format.")
    parser.add_option("-o","--output",action="store",dest="output_file",help="output file.")
    parser.add_option("-s","--start",action="store",dest="start_codons",default='ATG',help="Start codon (DNA sequence, so use 'T' instead of 'U') used to define open reading frame (ORF). default=%default")
    parser.add_option("-t","--stop",action="store",dest="stop_codons",default='TAG,TAA,TGA',help="Stop codon (DNA sequence, so use 'T' instead of 'U') used to define open reading frame (ORF). Multiple stop codons should be separated by ','. default=%default")
    
    (options, args) = parser.parse_args()

    if not options.input_file or not options.output_file:
        parser.print_help()
        sys.exit(0)

    count = 0        
    TMP = open(options.output_file, 'w')
    
    # Adding column names
    print("ID,ORF_coverage", file=TMP)

    for record in SeqIO.parse(options.input_file, "fasta"):
        count += 1
        sname = record.id
        seq = str(record.seq)
        coverage = extract_feature_from_seq(seq=seq, stt=options.start_codons, stp=options.stop_codons)
        row = [sname, str(coverage)]
        print(','.join(row), file=TMP)
        print(f"{count} genes finished\r", file=sys.stderr, end=' ')
    TMP.close()

if __name__ == '__main__':
    main()
