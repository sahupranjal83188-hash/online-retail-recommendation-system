import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ─────────────────────────────────────────
# 1. Loading the Dataset
# ─────────────────────────────────────────
data = pd.read_csv("online_retail.csv", encoding='ISO-8859-1')
print(data.head())

# ─────────────────────────────────────────
# 2. Data Description
# ─────────────────────────────────────────
print(data.info())
print(data.describe())

# ─────────────────────────────────────────
# 3. Data Cleaning
# ─────────────────────────────────────────

# Removing missing values
data.dropna(inplace=True)

# Removing cancelled orders (negative quantities)
data = data[data['Quantity'] > 0]

# ─────────────────────────────────────────
# 4. Creating Pivot Table
# ─────────────────────────────────────────
pivot_table = data.pivot_table(
    index='CustomerID',
    columns='Description',
    values='Quantity',
    aggfunc='sum',
    fill_value=0
)
print(pivot_table.head())

# ─────────────────────────────────────────
# 5. Popular Items — Globally
# ─────────────────────────────────────────
popular_global = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False)
print("Top 10 Global Products:")
print(popular_global.head(10))

# ─────────────────────────────────────────
# 6. Popular Items — Country-wise
# ─────────────────────────────────────────
popular_country = data.groupby(['Country', 'Description'])['Quantity'].sum().reset_index()
popular_country = popular_country.sort_values(by='Quantity', ascending=False)
print("Top products by country:")
print(popular_country.head(10))

# ─────────────────────────────────────────
# 7. Popular Items — Month-wise
# ─────────────────────────────────────────
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data['Month'] = data['InvoiceDate'].dt.month

popular_month = data.groupby(['Month', 'Description'])['Quantity'].sum().reset_index()
popular_month = popular_month.sort_values(by='Quantity', ascending=False)
print("Top products by month:")
print(popular_month.head(10))

# ─────────────────────────────────────────
# 8. Recommendation Function
# ─────────────────────────────────────────
def recommend_product(product_name, n=5):
    """
    Returns top n product recommendations based on
    Pearson correlation with the given product.

    Parameters:
        product_name (str): Name of the product to base recommendations on.
        n (int): Number of recommendations to return (default: 5).

    Returns:
        pandas.Series: Correlated products with their correlation scores.
    """
    if product_name not in pivot_table.columns:
        return "Product not found!"

    product_corr = pivot_table.corrwith(pivot_table[product_name])
    product_corr = product_corr.dropna().sort_values(ascending=False)

    return product_corr.head(n)

# ─────────────────────────────────────────
# 9. Example — Predicting Recommendations
# ─────────────────────────────────────────
print("\nRecommended products for 'WHITE HANGING HEART T-LIGHT HOLDER':")
print(recommend_product("WHITE HANGING HEART T-LIGHT HOLDER"))

# ─────────────────────────────────────────
# 10. Visualization — Top 10 Popular Products
# ─────────────────────────────────────────
plt.figure(figsize=(10, 5))
sns.barplot(
    x=popular_global.head(10).values,
    y=popular_global.head(10).index
)
plt.title("Top 10 Popular Products")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Description")
plt.tight_layout()
plt.show()
