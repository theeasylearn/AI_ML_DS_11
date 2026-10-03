import pandas as pd
import numpy as np 
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import kagglehub

# Download latest version
path = kagglehub.dataset_download("varshinipallerla/food-delivery")
print("Path to dataset files:", path)
#load dataset 

df = pd.read_csv(path + "/food_delivery_dataset.csv")
# One-hot encodes while keeping original column names as prefixes (e.g., Payment_Cash, Payment_Card)
#Categorical encoding
df_encoded = pd.get_dummies(df, prefix_sep=': ')
print(df_encoded.head(10))
# Find frequent itemsets
frequent_itemsets = apriori(
    df_encoded,
    min_support=0.10,
    use_colnames=True
)
print("\nFREQUENT ITEMSETS")
print(frequent_itemsets)
exit(1)
# # exit(1)
# # Generate association rules
# rules = association_rules(frequent_itemsets,metric="confidence",min_threshold=0.30)
# print("\nASSOCIATION RULES")
# for _,rule in rules.iterrows():
#     print(rule['antecedents']," -> ",rule['consequents'])
#     print(f"Support: {rule['support']:.2%}")
#     print(f"Confidence: {rule['confidence']:.2%}")
#     print(f"Lift: {rule['lift']:.2f}")
#     print("-" * 40)
# # exit(1)
# # Find strong rules
# strong_rules = rules[(rules["confidence"] >= 0.60) & (rules["lift"] > 1)]
# #variable = dataframe[condition]
# print("\nSTRONG RULES")
# for _,rule in strong_rules.iterrows():
#     print(rule['antecedents']," -> ",rule['consequents'])
#     print(f"Support: {rule['support']:.2%}")
#     print(f"Confidence: {rule['confidence']:.2%}")
#     print(f"Lift: {rule['lift']:.2f}")
#     print("-" * 40)