import pandas as pd

# Load data
df = pd.read_csv("techmart_sales.csv")
print("Shape:", df.shape)
print(df.head())

# ── Missing Data ──────────────────────────────────────────────
print("\nMissing values:")
print(df.isnull().sum())

df["Discount"] = df["Discount"].fillna(0)

# ── New Columns ───────────────────────────────────────────────
df["Gross_Revenue"] = df["Units_Sold"] * df["Unit_Price"]
df["Net_Revenue"]   = df["Gross_Revenue"] * (1 - df["Discount"])
df["Profit"]        = df["Net_Revenue"] * 0.25   # 25% profit margin

print("\nUpdated columns:")
print(df[["Order_ID", "Gross_Revenue", "Net_Revenue", "Profit"]].head())

# ── Q1: Revenue by Region ─────────────────────────────────────
print("\nRevenue by Region:")
print(df.groupby("Region")["Net_Revenue"].sum().sort_values(ascending=False))

# ── Q2: Top 3 Products ────────────────────────────────────────
print("\nTop 3 Products by Units Sold:")
print(df.groupby("Product")["Units_Sold"].sum().sort_values(ascending=False).head(3))

# ── Q3: Revenue by Category ───────────────────────────────────
print("\nRevenue by Category:")
print(df.groupby("Category")["Net_Revenue"].sum().sort_values(ascending=False))

# ── Q4: Salesperson Performance ───────────────────────────────
print("\nSalesperson Performance:")
print(df.groupby("Salesperson")[["Net_Revenue", "Profit"]].sum().round(2))

# ── Q5: Corporate vs Retail ───────────────────────────────────
print("\nCorporate vs Retail:")
print(df.groupby("Customer_Type")["Net_Revenue"].sum())

# ── Q6: Pivot Table ───────────────────────────────────────────
print("\nPivot – Region vs Category:")
pivot = pd.pivot_table(df, values="Net_Revenue", index="Region",
                       columns="Category", aggfunc="sum").round(2)
print(pivot)

# ── Summary ───────────────────────────────────────────────────
print("\n--- SUMMARY ---")
print(f"Total Orders  : {len(df)}")
print(f"Gross Revenue : {df['Gross_Revenue'].sum():,.2f}")
print(f"Net Revenue   : {df['Net_Revenue'].sum():,.2f}")
print(f"Total Profit  : {df['Profit'].sum():,.2f}")
