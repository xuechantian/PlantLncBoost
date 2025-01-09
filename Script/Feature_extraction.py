import os
import pandas as pd
import argparse

#
current_script_path = os.path.dirname(os.path.abspath(__file__))

#
fourier_average_path = os.path.join(current_script_path, "Fourier_average.py")
fourier_amplitude_path = os.path.join(current_script_path, "Fourier_amplitude.py")
orf_coverage_path = os.path.join(current_script_path, "ORF_coverage.py")

#
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Input FASTA file', required=True)
parser.add_argument('-o', '--output', help='Output CSV file', required=True)
args = parser.parse_args()
input_file = args.input
output_file = args.output

#
os.system(f"python {fourier_average_path} -i {input_file} -o Fourier1_lncRNA.csv -l lncRNA -r 6")

#
os.system(f"python {fourier_amplitude_path} -i {input_file} -o Fourier2_lncRNA.csv -l lncRNA -r 7")

#
os.system(f"python {orf_coverage_path} -i {input_file} -o ORF_lncRNA.csv")

#
fourier1 = pd.read_csv("Fourier1_lncRNA.csv", header=None, names=["nameseq", "average"])
fourier2 = pd.read_csv("Fourier2_lncRNA.csv", header=None, names=["nameseq", "amplitude"])
orf = pd.read_csv("ORF_lncRNA.csv", header=None, names=["nameseq", "ORF_coverage"])

merged = pd.merge(fourier1, fourier2, on="nameseq")
merged = pd.merge(merged, orf, on="nameseq")

# 
result = merged[["nameseq", "average", "amplitude", "ORF_coverage"]]
result.to_csv(output_file, index=False)

