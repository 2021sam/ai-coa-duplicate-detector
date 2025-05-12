import pandas as pd
from difflib import SequenceMatcher
import csv

# Load COA.csv and filter only ACCNT rows
with open("COA.csv", newline="", encoding='utf-8-sig') as f:
    reader = list(csv.reader(f))
    accnt_rows = [row for row in reader if row and row[0].strip() == "ACCNT"]

# Convert to DataFrame
columns = ["TYPE", "NAME", "REFNUM", "TIMESTAMP", "ACCNTTYPE", "OBAMOUNT",
           "DESC", "ACCNUM", "SCD", "BANKNUM", "EXTRA", "HIDDEN", "DELCOUNT", "USEID"]
df = pd.DataFrame(accnt_rows, columns=columns)

# Add blank columns for tracking duplicates
df["DuplicateOf"] = ""
df["Similarity"] = ""

# Similarity detection
threshold = 0.85  # adjust as needed
for i in range(len(df)):
    name1 = df.loc[i, "NAME"]
    for j in range(i + 1, len(df)):
        name2 = df.loc[j, "NAME"]
        score = SequenceMatcher(None, name1.lower(), name2.lower()).ratio()
        if score >= threshold:
            # Mark both directions for ease of reference
            df.at[i, "DuplicateOf"] = name2
            df.at[i, "Similarity"] = f"{round(score*100, 2)}%"
            df.at[j, "DuplicateOf"] = name1
            df.at[j, "Similarity"] = f"{round(score*100, 2)}%"

# Output to a new file
df.to_csv("COA_duplicates_marked.csv", index=False, encoding="utf-8-sig")
print("✅ Duplicate detection complete. File saved as COA_duplicates_marked.csv")
