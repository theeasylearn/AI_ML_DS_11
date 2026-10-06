import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import kagglehub
# pip install openpyxl
# Download dataset
path = kagglehub.dataset_download("varshinipallerla/food-delivery")

# Load dataset
df = pd.read_csv(path + "/food_delivery_dataset.csv")

# 2. Select categorical/string columns to analyze for associations
columns_of_interest = [
    'preferred_cuisine', 
    'delivery_method', 
    'weather_condition', 
    'traffic_condition'
]
subset_df = df[columns_of_interest]

# 3. Transform string values into a boolean transaction matrix (One-Hot Encoding)
# 'delivery_method_Car', 'weather_condition_Snowy', etc., become 0/1 columns
basket = pd.get_dummies(subset_df)

# 4. Apply the Apriori algorithm 
# min_support=0.05 targets itemsets appearing in at least 5% of all orders
frequent_itemsets = apriori(basket, min_support=0.05, use_colnames=True)

# 5. Generate association rules based on the frequent itemsets
# Sorting by 'lift' highlights the strongest correlations relative to random chance
rules_df = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# 1. Create a column that combines antecedent and consequent into an unordered set
rules_df['itemset_pair'] = rules_df.apply(
    lambda x: frozenset([x['antecedents'], x['consequents']]), axis=1
)

# 2. Sort by confidence (highest first)
filtered_rules = rules_df.sort_values(by='confidence', ascending=False)

# 3. Drop duplicates based on the unordered pair, keeping only the first (highest confidence)
filtered_rules = filtered_rules.drop_duplicates(subset=['itemset_pair'], keep='first')

# 4. Clean up the helper column and sort by lift for the final view
filtered_rules = filtered_rules.drop(columns=['itemset_pair']).sort_values(by='lift', ascending=False)

print(filtered_rules[['antecedents','consequents','support','confidence','lift']])
for _,rule in filtered_rules.iterrows():
    print("".join(rule['antecedents']),end=' ')
    print("".join(rule['consequents']),end=' ')
    print(round(rule['support'],2),end=' ')
    print(round(rule['confidence'],2),end=' ')
    print(round(rule['lift'],2))
    print("-"*100)

#writing data into excel file 

# 1. Convert frozensets to comma-separated strings for Excel compatibility
filtered_rules['antecedents'] = filtered_rules['antecedents'].apply(lambda item: ','.join(list(item)))

filtered_rules['consequents'] = filtered_rules['consequents'].apply(lambda item: ', '.join(list(item)))

# 2. (Optional) Round the numerical metrics to an exact number of decimal places
numeric_columns = [ 'support', 'confidence', 'lift']
for col in numeric_columns:
    if col in filtered_rules.columns:
        filtered_rules[col] = filtered_rules[col].round(2)

# write all columns to files 
# filtered_rules.to_excel("filtered_rules.xlsx", index=False)

#write only selected columns into files
file_name = "filtered_rules.xlsx"
filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].to_excel(file_name, index=False)

