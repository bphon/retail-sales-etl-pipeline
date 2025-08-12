import pandas as pd

# Extract
df = pd.read_csv('data/sales_data.csv')

# Transform
df['total'] = df['quantity'] * df['price']

# Load (print or save)
df.to_csv('data/sales_transformed.csv', index=False)
print("ETL process complete. Data saved to data/sales_transformed.csv")
