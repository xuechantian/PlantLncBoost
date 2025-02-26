![PlantLncBoost](https://github.com/xuechantian/PlantLncBoost/blob/master/PlantLncBoost.workflow.png) 

# PlantLncBoost: A Machine Learning Based Model for Plant Long Non-coding RNA Identification

![PlantLncBoost](https://github.com/xuechantian/PlantLncBoost/blob/master/PlantLncBoost.workflow.png) 

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
- **Integration Ready**: Can be incorporated into larger RNA-seq analysis pipelines

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Dependencies

PlantLncBoost requires the following Python packages:
```
numpy>=1.18.0
pandas>=1.0.0
scikit-learn>=0.22.0
catboost>=0.24.0
biopython>=1.76
```

### Install from GitHub

```bash
# Clone the repository
git clone https://github.com/xuechantian/PlantLncBoost.git

# Navigate to the directory
cd PlantLncBoost

# Install the dependencies
pip install -r requirements.txt

# Install the need packages
pip install .
```


## Usage

### **Feature extraction

    python ./PlantLncBoost/Script/Feature_extraction.py -i ./PlantLncBoost/data/test.fasta -o PlantLncBoost_feature.csv

### **LncRNA prediction
In the second column (Predicted_label) of the result file, 1 represents lncRNA and 0 represents mRNA

    python ./PlantLncBoost/Script/PlantLncBoost_prediction.py -i PlantLncBoost_feature.csv -m ./PlantLncBoost/Model/PlantLncBoost_model.cb -t 0.5 -o PlantLncBoost_prediction.csv
```



## Troubleshooting

### Common Issues

1. **Memory Errors**: When processing very large files, try increasing batch size or using the `--low_memory` flag
2. **Invalid Sequences**: The tool will skip invalid sequences but report them in the log
3. **Model Loading Errors**: Ensure you have the correct model file path and version

### Error Messages

- `Error: Invalid sequence format` - Check that your FASTA file is properly formatted
- `Error: Model file not found` - Verify the path to the model file
- `Warning: N ambiguous nucleotides detected` - Sequences with N's will be processed but may have lower accuracy


## Citing PlantLncBoost

If you use PlantLncBoost in your research, please cite:
```
Tian X, et al. (2025). PlantLncBoost: A Machine Learning Based Model for Plant Long Non-coding RNA Identification. 
```

## Contact

* **Email:** xuechan.tian@bjfu.edu.cn;  jianfeng.mao@umu.se


