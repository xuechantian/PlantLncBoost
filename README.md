![PlantLncBoost](https://github.com/xuechantian/PlantLncBoost/blob/master/PlantLncBoost.workflow.png) 

# PlantLncBoost: A Machine Learning Based Model for Plant Long Non-coding RNA Identification


**Contact Information:**  
- Email: xuechan.tian@bjfu.edu.cn  
- Email: jianfeng.mao@umu.se


## Table of Contents
- [1. Introduction](#1-introduction)
- [2. Features](#2-features)
- [3. Installation](#3-installation)
  - [3.1 Prerequisites](#31-prerequisites)
  - [3.2 Dependencies](#32-dependencies)
  - [3.3 Install PlantLncBoost](#33-install-from-github)
- [4. Usage](#4-usage)
  - [4.1 Set Environment Variable](#41-set-environment-variable)
  - [4.2 Feature extraction](#42-feature-extraction)
  - [4.3 LncRNA prediction](#43-lncrna-prediction)
- [5. Error Messages](#5-error-messages)
- [6. Citing PlantLncBoost](#6-citing-plantlncboost)

  
## 1. Introduction

PlantLncBoost is a machine learning-based model for identifying long non-coding RNAs (lncRNAs) in plants. Built on the powerful gradient boosting framework CatBoost, PlantLncBoost offers high accuracy and performance in distinguishing plant lncRNAs from protein-coding RNAs. Unlike many existing tools that were primarily developed for animal lncRNAs, PlantLncBoost is specifically trained and optimized for plant genomes, taking into account their unique characteristics and sequence features.

This tool is designed for computational biologists, plant genomics researchers, and bioinformaticians who need accurate lncRNA identification for plant genome annotation, functional genomics studies, or comparative transcriptomics.

## 2. Features

- **Plant-Specific Optimization**: Trained specifically on plant transcriptomes to account for plant-specific lncRNA characteristics
- **High-Performance Machine Learning**: Leverages CatBoost's gradient boosting framework for superior accuracy and speed
- **Comprehensive Feature Set**: Integrates sequence-derived feature and Fourier-based features including:
  - Open Reading Frame (ORF) Coverage
  - Complex_Fourier_average
  - Atomic_Fourier_amplitude

## 3. Installation

### 3.1 Prerequisites

- Python 3.7

### 3.2 Install Dependencies

#### PlantLncBoost requires the following Python packages:
    Python (>=3.7)
    Biopython
    NumPy
    Pandas
    SciPy
    CatBoost

#### Create and activate a conda environment
    conda create -n lncrna_env python=3.7
    conda activate lncrna_env
#### Install core dependencies
    conda install -c conda-forge biopython numpy pandas scipy catboost
    
### 3.3 Install PlantLncBoost

#### Clone the repository
    git clone https://github.com/xuechantian/PlantLncBoost.git



## 4. Usage
### 4.1 Set Environment Variable
Set the installation path of PlantLncBoost in your environment:

    export PLANTLNCBOOST="/path/to/PlantLncBoost/"

### 4.2 Feature extraction
    python "${PLANTLNCBOOST}/Script/Feature_extraction.py" -i "${PLANTLNCBOOST}/data/test.fasta" -o PlantLncBoost_feature.csv


### 4.3 LncRNA prediction

In the second column (Predicted_label) of the result file, 1 represents lncRNA and 0 represents mRNA

    python "${PLANTLNCBOOST}/Script/PlantLncBoost_prediction.py" -i PlantLncBoost_feature.csv -m "${PLANTLNCBOOST}/Model/PlantLncBoost_model.cb" -t 0.5 -o PlantLncBoost_prediction.csv


## 5. Error Messages

- `Error: Invalid sequence format` - Check that your FASTA file is properly formatted
- `Error: Model file not found` - Verify the path to the model file. Ensure you have the correct model file path and version
- `Warning: N ambiguous nucleotides detected` - Sequences with N's will be processed but may have lower accuracy


## 6. Citing PlantLncBoost
    Tian X, et al. (2025). , et al. (2025). PlantLncBoost: A Machine Learning Based Model for Plant Long Non-coding RNA Identification. 


