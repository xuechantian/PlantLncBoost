#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import scipy.stats
import statistics
import argparse
from Bio import SeqIO
from scipy.fftpack import fft, ifft
import warnings
warnings.filterwarnings("ignore")


#############################################################################
#############################################################################

def header():
    dataset = open(foutput, 'a')
    dataset.write("nameseq,amplitude")  
    dataset.write("\n")
    return

        
def file_record():
    dataset = open(foutput, 'a')
    dataset.write("%s,%s\n" % (str(name_seq), features[12]))  
    print("Sequence Analyzed!!")
    return


def feature_extraction():
    global features
    features = []
    average = sum(spectrum)/len(spectrum)
    features.append(average)
    median = np.median(spectrum)
    features.append(median)
    maximum = np.max(spectrum)
    features.append(maximum)
    minimum = np.min(spectrum)
    features.append(minimum)
    peak = (len(spectrum)/3)/(average)
    features.append(peak)
    peak_two = (len(spectrumTwo)/3)/(np.mean(spectrumTwo))
    features.append(peak_two)
    standard_deviation = np.std(spectrum)
    features.append(standard_deviation)
    standard_deviation_pop = statistics.stdev(spectrum)
    features.append(standard_deviation_pop)
    percentile15 = np.percentile(spectrum, 15)
    features.append(percentile15)
    percentile25 = np.percentile(spectrum, 25)
    features.append(percentile25)
    percentile50 = np.percentile(spectrum, 50)
    features.append(percentile50)
    percentile75 = np.percentile(spectrum, 75)
    features.append(percentile75)
    amplitude = maximum - minimum
    features.append(amplitude)
    variance = statistics.variance(spectrum)
    features.append(variance)
    interquartile_range = np.percentile(spectrum, 75) - np.percentile(spectrum, 25)
    features.append(interquartile_range)
    semi_interquartile_range = (np.percentile(spectrum, 75) - np.percentile(spectrum, 25))/2 
    features.append(semi_interquartile_range)
    coefficient_of_variation = standard_deviation/average
    features.append(coefficient_of_variation)
    skewness = (3 * (average - median))/standard_deviation
    features.append(skewness)   
    kurtosis = (np.percentile(spectrum, 75) - np.percentile(spectrum, 25)) / (2 * (np.percentile(spectrum, 90) - np.percentile(spectrum, 10))) 
    features.append(kurtosis)
    return


def binary_fourier():
    header()
    global spectrum, spectrumTwo, name_seq
    for seq_record in SeqIO.parse(finput, "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        spectrum = []
        spectrumTwo = []
        A = []
        C = []
        T = []
        G = []
        for nucle in seq:
            if nucle == "A":
                A.append(1)
            else:
                A.append(0)
            if nucle == "C":
                C.append(1)
            else:
                C.append(0)
            if nucle == "T" or nucle =="U":
                T.append(1)
            else:
                T.append(0)
            if nucle == "G":
                G.append(1)
            else:
                G.append(0)
        FA = fft(A)
        FC = fft(C)
        FT = fft(T)
        FG = fft(G)
        for i in range(len(seq)):
            specTotal = (abs(FA[i])**2) + (abs(FC[i])**2) + (abs(FT[i])**2) + (abs(FG[i])**2)
            specTwo = (abs(FA[i])) + (abs(FC[i])) + (abs(FT[i])) + (abs(FG[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction()
        file_record()
    return


def zcurve_fourier():
    header()
    global spectrum, spectrumTwo, name_seq
    for seq_record in SeqIO.parse(finput, "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        spectrum = []
        spectrumTwo = []
        R = 0
        Y = 0
        M = 0
        K = 0
        W = 0
        S = 0
        x = []
        y = []
        z = []
        for nucle in seq:
            if nucle == "A" or nucle == "G":
                R += 1
                x.append((R)-(Y))
            else:
                Y += 1
                x.append((R)-(Y))
            if nucle == "A" or nucle == "C":
                M += 1
                y.append((M)-(K))
            else:
                K += 1
                y.append((M)-(K))
            if nucle == "A" or nucle == "T" or nucle == "U":
                W += 1
                z.append((W)-(S))
            else:
                S += 1
                z.append((W)-(S))
        FX = fft(x)
        FY = fft(y)
        FZ = fft(z)
        for i in range(len(seq)):
            specTotal = (abs(FX[i])**2) + (abs(FY[i])**2) + (abs(FZ[i])**2)
            specTwo = (abs(FX[i])) + (abs(FY[i])) + (abs(FZ[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction()
        file_record()
    return


def integer_fourier():
    header()
    global spectrum, spectrumTwo, name_seq
    for seq_record in SeqIO.parse(finput, "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        spectrum = []
        spectrumTwo = []
        integer = []
        for nucle in seq:
            if nucle == "T" or nucle == "U":
                integer.append(0)
            elif nucle == "C":
                integer.append(1)
            elif nucle == "A":
                integer.append(2)
            else:
                integer.append(3)
        FI = fft(integer)
        for i in range(len(seq)):
            specTotal = (abs(FI[i])**2)
            specTwo = (abs(FI[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction()
        file_record()
    return


def real_fourier():
    header()
    global spectrum, spectrumTwo, name_seq
    for seq_record in SeqIO.parse(finput, "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        spectrum = []
        spectrumTwo = []
        real = []
        for nucle in seq:
            if nucle == "T" or nucle == "U":
                real.append(1.5)
            elif nucle == "C":
                real.append(0.5)
            elif nucle == "A":
                real.append(-1.5)
            else:
                real.append(-0.5)
        FR = fft(real)
        for i in range(len(seq)):
            specTotal = (abs(FR[i])**2)
            specTwo = (abs(FR[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction()
        file_record()
    return


def eiip_fourier():
    header()
    global spectrum, spectrumTwo, name_seq
    for seq_record in SeqIO.parse(finput, "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        spectrum = []
        spectrumTwo = []
        eiip = []
        for nucle in seq:
            if nucle == "T" or nucle == "U":
                eiip.append(0.1335)
            elif nucle == "C":
                eiip.append(0.1340)
            elif nucle == "A":
                eiip.append(0.1260)
            else:
                eiip.append(0.0806)
        Feiip = fft(eiip)
        for i in range(len(seq)):
            specTotal = (abs(Feiip[i])**2)
            specTwo = (abs(Feiip[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction()
        file_record()
    return


def complex_number():
    header()
    global spectrum, spectrumTwo, name_seq
    for seq_record in SeqIO.parse(finput, "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        spectrum = []
        spectrumTwo = []
        complexNumber = []
        for nucle in seq:
            if nucle == "T" or nucle == "U":
                complexNumber.append(1-1j)
            elif nucle == "C":
                complexNumber.append(-1+1j)
            elif nucle == "A":
                complexNumber.append(1+1j)
            else:
                complexNumber.append(-1-1j)
        FcomplexNumber = fft(complexNumber)
        for i in range(len(seq)):
            specTotal = (abs(FcomplexNumber[i])**2)
            specTwo = (abs(FcomplexNumber[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction()
        file_record()
    return


def atomic_number():
    header()
    global spectrum, spectrumTwo, name_seq
    for seq_record in SeqIO.parse(finput, "fasta"):
        seq = seq_record.seq
        seq = seq.upper()
        name_seq = seq_record.name
        spectrum = []
        spectrumTwo = []
        atomicNumber = []
        for nucle in seq:
            if nucle == "T" or nucle == "U":
                atomicNumber.append(66)
            elif nucle == "C":
                atomicNumber.append(58)
            elif nucle == "A":
                atomicNumber.append(70)
            else:
                atomicNumber.append(78)
        FatomicNumber = fft(atomicNumber)
        for i in range(len(seq)):
            specTotal = (abs(FatomicNumber[i])**2)
            specTwo = (abs(FatomicNumber[i]))
            spectrum.append(specTotal)
            spectrumTwo.append(specTwo)
        feature_extraction()
        file_record()
    return


#############################################################################    
if __name__ == "__main__":
    print("\n")
    print("###################################################################################")
    print("########## Feature Extraction: Fourier Amplitude (nameseq & amplitude only) #######")
    print("##########    Arguments: -i input -o output [-l label] -r representation  #########")  # 修改帮助信息
    print("########## -r:  1 = Binary, 2 = Z-curve, 3 = Real, 4 = Integer, 5 = EIIP  #########")
    print("##########                6 = ComplexNumber, 7 = Atomic Number          ###########")
    print("##########                 Author: Robson Parmezan Bonidia              ###########")
    print("###################################################################################")
    print("\n")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Fasta format file | E.g., test.fasta', required=True)
    parser.add_argument('-o', '--output', help='Csv format file | E.g., output.csv', required=True)
    parser.add_argument('-l', '--label', help='[Optional] Dataset Label | E.g., lncRNA, mRNA', required=False)  # 标记为可选
    parser.add_argument('-r', '--representation', help='1-7 (as listed above)', type=int, required=True)
    args = parser.parse_args()
    
    finput = args.input
    foutput = args.output
    label_dataset = args.label  # 参数被解析但不使用
    representation = args.representation
    
    if representation == 1:
        binary_fourier()
    elif representation == 2:
        zcurve_fourier()
    elif representation == 3:
        real_fourier()
    elif representation == 4:
        integer_fourier()
    elif representation == 5:
        eiip_fourier()
    elif representation == 6:
        complex_number()
    elif representation == 7:
        atomic_number()
    else:
        print("Invalid representation option. Choose 1-7.")

