# online-retail-recommendation-system
# 🛒 Online Retail Product Recommendation System

A Data Science project that analyzes online retail transaction data to uncover popular products and generate personalized product recommendations using correlation-based filtering.

---

## 📌 Objective

The goal of this project is to:
- Analyze an online retail dataset to find **globally**, **country-wise**, and **month-wise** popular products
- Build a **product recommendation system** using correlation-based filtering
- Visualize the top-selling products using charts

---

## 📂 Dataset

- **Source:** [Kaggle](https://www.kaggle.com/)
- **File:** `online_retail.csv`
- **Encoding:** ISO-8859-1

### Dataset Columns:
| Column | Description |
|---|---|
| InvoiceNo | Unique invoice number |
| StockCode | Product stock code |
| Description | Product name/description |
| Quantity | Number of units purchased |
| InvoiceDate | Date and time of purchase |
| UnitPrice | Price per unit |
| CustomerID | Unique customer identifier |
| Country | Country of the customer |

---

## 🛠️ Tools & Libraries Used

| Tool / Library | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, and manipulation |
| `numpy` | Numerical operations |
| `seaborn` | Data visualization (bar charts) |
| `matplotlib` | Plotting and rendering charts |
| `Python` | Core programming language |

---

## ⚙️ How It Works

### 1. Data Loading & Preprocessing
- The dataset is loaded using `pandas.read_csv()` with ISO-8859-1 encoding.
- Missing values are dropped using `dropna()`.
- Cancelled orders (negative quantities) are removed by filtering rows where `Quantity > 0`.

### 2. Pivot Table Creation
- A pivot table is created with `CustomerID` as rows and `Description` (product names) as columns.
- Cell values represent the total quantity purchased by each customer for each product.
- This forms the base matrix for correlation-based recommendations.

### 3. Popular Products Analysis
- **Global Popularity:** Products are grouped by `Description` and total `Quantity` is summed and sorted.
- **Country-wise Popularity:** Products are grouped by `Country` and `Description` to find top sellers per region.
- **Month-wise Popularity:** `InvoiceDate` is converted to datetime, the month is extracted, and products are grouped by month to find seasonal trends.

### 4. Recommendation Function
```python
def recommend_product(product_name, n=5):
    product_corr = pivot_table.corrwith(pivot_table[product_name])
    product_corr = product_corr.dropna().sort_values(ascending=False)
    return product_corr.head(n)
```
- Uses **Pearson correlation** between product purchase vectors across customers.
- For a given product, finds the top `n` most correlated products — i.e., products frequently bought together by the same customers.

### 5. Visualization
- A horizontal bar chart is plotted using `seaborn` and `matplotlib` to display the **Top 10 Most Popular Products** globally.

---

## 📊 Sample Output

### Top 10 Global Products:
| Product | Total Quantity |
|---|---|
| PAPER CRAFT, LITTLE BIRDIE | 80,995 |
| MEDIUM CERAMIC TOP STORAGE JAR | 77,916 |
| WORLD WAR 2 GLIDERS ASSTD DESIGNS | 54,415 |
| JUMBO BAG RED RETROSPOT | 46,181 |
| WHITE HANGING HEART T-LIGHT HOLDER | 36,725 |

### Recommendations for `WHITE HANGING HEART T-LIGHT HOLDER`:
| Product | Correlation Score |
|---|---|
| WHITE HANGING HEART T-LIGHT HOLDER | 1.000000 |
| GIN + TONIC DIET METAL SIGN | 0.750247 |
| RED HANGING HEART T-LIGHT HOLDER | 0.657817 |
| WASHROOM METAL SIGN | 0.642895 |
| LAUNDRY 15C METAL SIGN | 0.641969 |

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install required libraries:
   ```bash
   pip install pandas numpy seaborn matplotlib
   ```

3. Place the `online_retail.csv` file in the project directory.

4. Run the script:
   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```
├── main.py               # Main Python script
├── online_retail.csv     # Dataset (download from Kaggle)
└── README.md             # Project documentation
```

---

## 👤 Author

Made as part of a **Major Project – Data Science**
