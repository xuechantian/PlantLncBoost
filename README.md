![PlantLncBoost](https://github.com/xuechantian/PlantLncBoost/blob/master/PlantLncBoost.workflow.png) 

# PlantLncBoost




### **PlantLncBoost is a novel computational tool designed for the prediction of plant long non-coding RNAs (lncRNAs). It addresses the challenge of poor sequence conservation across species by employing advanced model selection, hyperparameter optimization, and feature selection. Key features such as ORF-Coverage, Complex_Fourier_average, and Atomic_Fourier_amplitude enhance its ability to accurately distinguish between coding and non-coding RNAs. PlantLncBoost exhibits superior performance compared to existing tools, enabling reliable detection of lncRNAs across a diverse range of plant species.**




#### **Email:** xuechan.tian@bjfu.edu.cn;  jianfeng.mao@umu.se



## **1. Dependencies
    Python (>=3.7.3)
    Biopython
    NumPy
    Pandas
    SciPy
    CatBoost


## **2. Usage

### **2.1 Feature extraction

    python ./PlantLncBoost/Script/Feature_extraction.py -i test.fasta -o PlantLncBoost_feature.csv

### **2.2 LncRNA prediction
In the second column (Predicted_label) of the result file, 1 represents lncRNA and 0 represents mRNA

    python ./PlantLncBoost/Script/PlantLncBoost_prediction.py -i PlantLncBoost_feature.csv -m ./PlantLncBoost/Model/PlantLncBoost_model.cb -t 0.5 -o PlantLncBoost_prediction.csv
