![PlantLncBoost](https://github.com/xuechantian/PlantLncBoost/blob/master/PlantLncBoost.workflow.png) 

# PlantLncBoost: A Machine Learning Based Model for Plant Long Non-coding RNA Identification


## Introduction

PlantLncBoost is a machine learning-based model for identifying long non-coding RNAs (lncRNAs) in plants. Built on the powerful gradient boosting framework CatBoost, PlantLncBoost offers high accuracy and performance in distinguishing plant lncRNAs from protein-coding RNAs. Unlike many existing tools that were primarily developed for animal lncRNAs, PlantLncBoost is specifically trained and optimized for plant genomes, taking into account their unique characteristics and sequence features.

This tool is designed for computational biologists, plant genomics researchers, and bioinformaticians who need accurate lncRNA identification for plant genome annotation, functional genomics studies, or comparative transcriptomics.

## Features

- **Plant-Specific Optimization**: Trained specifically on plant transcriptomes to account for plant-specific lncRNA characteristics
- **High-Performance Machine Learning**: Leverages CatBoost's gradient boosting framework for superior accuracy and speed
- **Comprehensive Feature Set**: Integrates sequence-derived feature and Fourier-based features including:
  - Open Reading Frame (ORF) Coverage
  - Complex_Fourier_average
  - Atomic_Fourier_amplitude

## Installation

### Prerequisites

- Python 3.7

### Dependencies

PlantLncBoost requires the following Python packages:
```
numpy
pandas
scikit-learn
catboost
biopython
```

### Install from GitHub

```bash
# Clone the repository
git clone https://github.com/xuechantian/PlantLncBoost.git

# Navigate to the directory
cd PlantLncBoost

# Install the dependencies
pip install .
```


## Usage
### Set Environment Variable
Set the installation path of PlantLncBoost in your environment:
    export PLANTLNCBOOST="/path/to/PlantLncBoost/"

### Feature extraction
    python "${PLANTLNCBOOST}/Script/Feature_extraction.py" -i "${PLANTLNCBOOST}/data/test.fasta" -o PlantLncBoost_feature.csv


### LncRNA prediction

In the second column (Predicted_label) of the result file, 1 represents lncRNA and 0 represents mRNA

    python "${PLANTLNCBOOST}/Script/PlantLncBoost_prediction.py" -i PlantLncBoost_feature.csv -m "${PLANTLNCBOOST}/Model/PlantLncBoost_model.cb" -t 0.5 -o PlantLncBoost_prediction.csv


## Troubleshooting

### Error Messages

- `Error: Invalid sequence format` - Check that your FASTA file is properly formatted
- `Error: Model file not found` - Verify the path to the model file. Ensure you have the correct model file path and version
- `Warning: N ambiguous nucleotides detected` - Sequences with N's will be processed but may have lower accuracy


### Citing PlantLncBoost
    Tian X, et al. (2025). , et al. (2025). PlantLncBoost: A Machine Learning Based Model for Plant Long Non-coding RNA Identification. 


### Contact

    Email: xuechan.tian@bjfu.edu.cn;  jianfeng.mao@umu.se


