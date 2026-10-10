import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
# STEP 2: LOAD DATASET
df = pd.read_csv('bank-full.csv')
print("\n DATASET SHAPE:")
print("before drop",df.shape)
# data cleaning
print("after drop",df.shape)
print("\nCOLUMNS:")
print(df.columns.tolist())
# exit(1)
#Binning(converting discrete values into categories)
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 60, 100], labels=['young', 'middle_aged', 'senior'])
df['balance_group'] = pd.cut(df['balance'], bins=[-9000, 0, 1000, 100000], labels=['negative', 'low', 'high'])
columns_to_mine = ['job', 'marital', 'education', 'housing', 'loan', 'y', 'age_group', 'balance_group']
df_subset = df[columns_to_mine]
df_encoded = pd.get_dummies(df_subset).astype(bool)
# print(df_encoded.head(10))
# exit(1)
#findout frequent symptom 
frequent_itemsets = fpgrowth(df_encoded,min_support=0.01,use_colnames=True)
rules = association_rules(frequent_itemsets,metric="confidence",min_threshold=0.05)
rules = rules[rules['lift']>1]
rules = rules.sort_values("lift",ascending=False)
# print(rules.columns)
for index,rule in rules.iterrows():
    print(f"{' '.join(rule['antecedents'])} -> {' '.join(rule['consequents'])} {round(rule['support'],2)} {round(rule['confidence'],2)} {round(rule['lift'],2)}")
#task export result into excel.
