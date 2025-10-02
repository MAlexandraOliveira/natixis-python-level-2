'''
CLASS 4 - POSSIBLE SOLUTION

COURSE PROJECT - CUSTOMER TRANSACTION ANALYTICS
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
TASK 1 - DATA PROCESSING
'''
# Load dataset
from data.sample_data import sample_data as customers

# Print customer info
for c in customers:
   print(
       f"ID: {c['customer_id']} | Age: {c['age']} | Region: {c['region']}\n\
Account: {c['account_type']} | Transactions: {len(c['transactions'])}")
   print()

# Helper function
def to_eur(amount, currency):
    """Convert amount to EUR if in USD (1 USD = 0.9 EUR)"""
    return amount * 0.9 if currency == "USD" else amount

# Compute total_spending (EUR) and top_category per customer and save in a list
rows = []

for c in customers:
    total_eur = 0.0
    by_category = {} 

    for t in c["transactions"]:
        amt_eur = to_eur(t["amount"], t["currency"])
        total_eur += amt_eur

        # update spending per category
        if t["category"] not in by_category:
            by_category[t["category"]] = 0.0
        by_category[t["category"]] += amt_eur

    # Determine top category
    if by_category:
        top_category = max(by_category, key=by_category.get)
    else:
        top_category = "Unknown"

    # Add row to list
    rows.append({
        "customer_id": c["customer_id"],
        "age": c["age"],
        "region": c["region"],
        "account_type": c["account_type"],
        "total_spending": round(total_eur, 2),
        "top_category": top_category,
    })

# Create DataFrame from rows
df = pd.DataFrame(rows)
print("\nCustomer summary:")
print(df.head())

# Total spending per region
region_spending = (
    df.groupby("region", as_index=False)["total_spending"]
      .sum()
      .sort_values("total_spending", ascending=False)
)
print("\nTotal spending per region (€):")
print(region_spending)

'''
TASK 2 - FUNCTIONS AND COMPREHENSIONS
'''

#average transaction in EUR
def avg_transaction(customer):
    amounts = [to_eur(t["amount"], t["currency"]) for t in customer["transactions"]]
    if amounts:  # avoid division by zero
        return round(sum(amounts) / len(amounts), 2)
    else:
        return 0.0

# Print first 5
for c in customers[:5]:
    print(f"Average transaction for {c['customer_id']}: {avg_transaction(c)} EUR")

# Add avg_transaction column to DataFrame
df["avg_transaction"] = [avg_transaction(c) for c in customers]
print("\nDataFrame with avg_transaction (head):")
print(df.head())

food_transactions = [
    to_eur(t["amount"], t["currency"])
    for c in customers
    for t in c["transactions"]
    if t["category"] == "Food"
]

print(f"\nNumber of Food transactions: {len(food_transactions)}")

# Create Series for pandas summary
food_series = pd.Series(food_transactions)
print("\nFood transaction stats:")
print(food_series.describe())

# Dictionary comprehension: {customer_id: total_spending}
spending_dict = {c["customer_id"]: c["total_spending"] for c in rows}

print("Total spending dict (first 5):", dict(list(spending_dict.items())[:5]))

print("\nCompare with DataFrame values:")
print(df[["customer_id", "total_spending"]].head())


'''
TASK 3 - Summary Report with Lambdas, Built-ins, and Generators
'''
summary_report = {}

# Total customers
summary_report["total_customers"] = len(df)

# Total spending (generator expression)
total = sum(x for x in df["total_spending"])
summary_report["total_spending_all"] = total

# Lowest spender (lambda with sort_values)
lowest = df.sort_values(by="total_spending", key=lambda s: s, ascending=True).iloc[0]
summary_report["lowest_spender"] = (lowest["customer_id"], lowest["total_spending"])

# Average spending
summary_report["avg_spending"] = round(total / len(df), 2)

# Spending by region (lambda inside groupby apply)
region_spending = df.groupby("region")["total_spending"].apply(lambda x: x.sum()).to_dict()
summary_report["spending_by_region"] = region_spending

# Top category overall (by median spending)
category_counts = df.groupby("top_category")["customer_id"].apply(lambda x: len(x))
print(category_counts)
top_category = max(category_counts.items(), key=lambda t: t[1])
summary_report["most_frequent_category"] = top_category

print(summary_report)

'''
TASK 4 - Data Visualization
'''

# MATPLOTLIB: Horizontal Bar Chart with Top 10 customers by spending
top10 = df.sort_values("total_spending", ascending=False).head(10)
plt.figure(figsize=(10,6))
plt.barh(top10["customer_id"], top10["total_spending"], color="skyblue")
plt.title("Top 10 Customers by Spending")
plt.xlabel("Spending (€)")
plt.gca().invert_yaxis()  # highest on top
plt.tight_layout()
plt.savefig("top10_customers.jpeg")  # saved as JPEG
plt.show()

# MATPLOTLIB: Pie chart with share of spending by region
region_spending = df.groupby("region")["total_spending"].sum()
plt.figure(figsize=(6,6))
plt.pie(region_spending, labels=region_spending.index, autopct="%1.1f%%", startangle=140)
plt.title("Share of Spending by Region")
plt.show()

# MATPLOTLIB: A bar chart with the median spending by category
category_medians = df.groupby("top_category")["total_spending"].median()
plt.figure(figsize=(8,6))
category_medians.plot(kind="bar", color="coral")
plt.title("Median Spending by Category")
plt.ylabel("Median Spending (€)")
plt.show()

# SEABORN: histogram of total spending 
plt.figure(figsize=(8,6))
sns.histplot(df["total_spending"], bins=20, kde=True, color="green")
plt.axvline(df["total_spending"].mean(), color="red", linestyle="--", label=f"Mean = {df['total_spending'].mean():.2f}")
plt.axvline(df["total_spending"].median(), color="blue", linestyle="--", label=f"Median = {df['total_spending'].median():.2f}")
plt.title("Distribution of Customer Spending")
plt.xlabel("Spending (€)")
plt.ylabel("Count")
plt.legend()
plt.show()

# SEABORN: A boxplot with the spending distribution by account type 
plt.figure(figsize=(8,6))
sns.boxplot(x="account_type", y="total_spending", data=df, palette="Set2")
plt.title("Spending by Account Type")
plt.ylabel("Spending (€)")
plt.tight_layout()
plt.savefig("spending_boxplot.png")  # saved as PNG
plt.show()

# SEABORN: scatter plot with age vs. spending, colored by top category
plt.figure(figsize=(8,6))
sns.scatterplot(x="age", y="total_spending", hue="top_category", data=df, palette="Set1")
plt.title("Customer Spending by Age and Category")
plt.xlabel("Age")
plt.ylabel("Total Spending (€)")
plt.legend(title="Top Category")
plt.show()