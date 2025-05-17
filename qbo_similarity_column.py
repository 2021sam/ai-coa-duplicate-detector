import pandas as pd
from difflib import SequenceMatcher

# Load QBO COA export CSV
df = pd.read_csv("Paint Productions, Inc._Account List.csv", skiprows=2, encoding='utf-8-sig')

# Drop rows where 'Full name' is empty or clearly a header row
df = df[df["Full name"].notna()]
df = df[~df["Full name"].str.lower().str.contains("productions|total", na=False)]

# Add blank columns for tracking duplicates
df["DuplicateOf"] = ""
df["Similarity"] = ""

# Similarity detection based on 'Full name'
threshold = 0.85  # adjust as needed
for i in range(len(df)):
    name1 = df.loc[i, "Full name"]
    for j in range(i + 1, len(df)):
        name2 = df.loc[j, "Full name"]
        score = SequenceMatcher(None, name1.lower(), name2.lower()).ratio()
        if score >= threshold:
            df.at[i, "DuplicateOf"] = name2
            df.at[i, "Similarity"] = f"{round(score * 100, 2)}%"
            df.at[j, "DuplicateOf"] = name1
            df.at[j, "Similarity"] = f"{round(score * 100, 2)}%"

# Save results
df.to_csv("qbo_COA_duplicates_marked.csv", index=False, encoding="utf-8-sig")
print("✅ Duplicate detection complete. File saved as COA_duplicates_marked.csv")
