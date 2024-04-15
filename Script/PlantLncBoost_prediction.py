import argparse
import pandas as pd
from catboost import CatBoostClassifier

# Create a command line argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help='Input file path')
parser.add_argument('-m', '--model', required=True, help='Model path')
parser.add_argument('-t', '--threshold', type=float, required=True, help='Threshold value')
parser.add_argument('-o', '--output', required=True, help='Output file path')
args = parser.parse_args()

# Read data
data = pd.read_csv(args.input)

# Extract feature
X_test = data.iloc[:, 1:]

# Loading model
model = CatBoostClassifier()
model.load_model(args.model)

# Classification of lncRNA and mRNA
y_pred_prob = model.predict_proba(X_test)
y_pred = (y_pred_prob[:, 1] > args.threshold).astype(int)

# Save the result
result_df = pd.DataFrame({'id': data.iloc[:, 0], 'Predicted_label': y_pred})
result_df.to_csv(args.output, sep='\t', index=False)
