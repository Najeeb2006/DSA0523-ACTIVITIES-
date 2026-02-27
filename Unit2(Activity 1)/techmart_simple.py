import pandas as pd

# Load the dataset
df = pd.read_csv("techmart_sales.csv")

# ── 1. View the Data ──────────────────────────────────────────
print("First 5 rows:")
print(df.head())

print("\nShape (rows, columns):", df.shape)

print("\nColumn Names:", list(df.columns))

# ── 2. Missing Values ─────────────────────────────────────────
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df["Discount"]       = df["Discount"].fillna(df["Discount"].mean())
df["Units_Sold"]     = df["Units_Sold"].fillna(df["Units_Sold"].mean())
df["Unit_Price"]     = df["Unit_Price"].fillna(df["Unit_Price"].mean())
df["Salesperson"]    = df["Salesperson"].fillna(df["Salesperson"].mode()[0])
df["Region"]         = df["Region"].fillna(df["Region"].mode()[0])
df["Payment_Method"] = df["Payment_Method"].fillna(df["Payment_Method"].mode()[0])

print("\nMissing Values After Cleaning:", df.isnull().sum().sum())

# ── 3. New Columns ────────────────────────────────────────────
df["Total_Sales"] = df["Units_Sold"] * df["Unit_Price"]
df["Revenue"]     = df["Total_Sales"] * (1 - df["Discount"])

print("\nSample Revenue Data:")
print(df[["Product", "Units_Sold", "Unit_Price", "Discount", "Revenue"]].head())

# ── 4. Group By Region ────────────────────────────────────────
print("\nTotal Revenue by Region:")
print(df.groupby("Region")["Revenue"].sum().round(2))

# ── 5. Group By Category ──────────────────────────────────────
print("\nTotal Revenue by Category:")
print(df.groupby("Category")["Revenue"].sum().round(2))

# ── 6. Best Salesperson ───────────────────────────────────────
print("\nRevenue by Salesperson:")
print(df.groupby("Salesperson")["Revenue"].sum().sort_values(ascending=False).round(2))

# ── 7. Top 3 Products by Units Sold ──────────────────────────
print("\nTop 3 Products (Units Sold):")
print(df.groupby("Product")["Units_Sold"].sum().sort_values(ascending=False).head(3))

# ── 8. Pivot Table ────────────────────────────────────────────
print("\nPivot Table - Revenue by Region & Category:")
pivot = pd.pivot_table(df, values="Revenue", index="Region",
                       columns="Category", aggfunc="sum").round(2)
print(pivot)

# ── 9. Filter – Corporate Orders Only ────────────────────────
corporate = df[df["Customer_Type"] == "Corporate"]
print("\nCorporate Orders Count:", len(corporate))
print("Corporate Total Revenue:", round(corporate["Revenue"].sum(), 2))

# ── 10. Summary ───────────────────────────────────────────────
print("\n===== SUMMARY =====")
print("Total Orders     :", len(df))
print("Total Revenue    :", round(df["Revenue"].sum(), 2))
print("Avg Order Value  :", round(df["Revenue"].mean(), 2))
print("Top Region       :", df.groupby("Region")["Revenue"].sum().idxmax())
print("Top Category     :", df.groupby("Category")["Revenue"].sum().idxmax())
