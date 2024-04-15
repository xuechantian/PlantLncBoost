import argparse
import pandas as pd
from catboost import CatBoostClassifier

# 创建命令行参数解析器
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help='输入文件路径')
parser.add_argument('-m', '--model', required=True, help='模型文件路径')
parser.add_argument('-t', '--threshold', type=float, required=True, help='阈值')
parser.add_argument('-o', '--output', required=True, help='输出文件路径')
args = parser.parse_args()

# 读取数据
data = pd.read_csv(args.input)

# 提取特征
X_test = data.iloc[:, 1:]  # 特征

# 加载模型
model = CatBoostClassifier()
model.load_model(args.model)

# 预测测试集结果的概率
y_pred_prob = model.predict_proba(X_test)

# 根据阈值对预测结果进行二分类
y_pred = (y_pred_prob[:, 1] > args.threshold).astype(int)

# 添加id列到结果数据框，并将id和预测结果一起保存到CSV文件
result_df = pd.DataFrame({'id': data.iloc[:, 0], 'Predicted Label': y_pred})
result_df.to_csv(args.output, sep='\t', index=False)
