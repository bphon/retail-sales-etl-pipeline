# Retail Sales Analysis

This notebook analyzes the transformed retail sales data.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('../data/sales_transformed.csv')

# Summary statistics
print(df.describe())

# Plot sales trend
df.groupby('date')['total'].sum().plot(kind='bar')
plt.title('Sales by Date')
plt.show()
```
