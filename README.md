# PlantLncBoost

## **1. Dependencies
    Python (>=3.7.3)
    Biopython
    NumPy
    Pandas
    SciPy
    CatBoost


## **2. Usage

### **2.1 Feature extraction

    python PlantLncBoost/Script/Feature_extraction.py -i test.fasta -o PlantLncBoost_feature.csv

### **2.2 LncRNA prediction
In the second column (Predicted_label) of the result file, 1 represents lncRNA and 0 represents mRNA

    python ./PlantLncBoost/Script/PlantLncBoost_prediction.py -i PlantLncBoost_feature.csv -m ./PlantLncBoost/Model/PlantLncBoost_model.cb -t 0.5 -o PlantLncBoost_prediction.csv
