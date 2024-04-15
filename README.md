# PlantLncBoost
##
2.2 Usage

    2.2.1 Feature extraction

python ./PlantLncBoost/Feature_extraction.py -i test.fasta -o Feature.csv

    2.2.2 Model prediction

python ./PlantLncBoost/PlantLncBoost_prediction.py -i Feature.csv -m ./PlantLncBoost/PlantLncBoost_model.cb -t 0.5 -o prediction.csv
