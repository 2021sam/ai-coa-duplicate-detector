import pandas as pd

# Load CSV, skipping metadata rows to get proper headers
df = pd.read_csv("Paint Productions, Inc._Account List.csv", skiprows=2)

# Normalize column names: strip spaces and convert to lowercase
df.columns = df.columns.str.strip().str.lower()

# Print normalized columns to confirm
print("Normalized Columns:", df.columns.tolist())

# Filter rows where 'full name' column is not empty or NaN
df = df[df["full name"].notna()].reset_index(drop=True)

# Show the first few rows for confirmation
print(df.head())
