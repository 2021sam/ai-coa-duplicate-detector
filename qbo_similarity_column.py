import pandas as pd
from difflib import SequenceMatcher

# ✅ Skip first 2 metadata rows
df = pd.read_csv("Paint Productions, Inc._Account List.csv", skiprows=2, encoding='utf-8-sig')

# ✅ Defensive: Ensure 'Full name' column exists
if "Full name" not in df.columns:
    raise ValueError("❌ 'Full name' column not found. Please check the CSV formatting.")

# ✅ Drop rows where 'Full name' is blank
df = df[df["Full name"].notna()]

# ✅ Add tracking columns
df["DuplicateOf"] = ""
df["Similarity"] = ""

# ✅ Similarity comparison logic
threshold = 0.8
for i in range(len(df)):
    name1 = df.iloc[i]["Full name"]
    for j in range(i + 1, len(df)):
        name2 = df.iloc[j]["Full name"]
        score = SequenceMatcher(None, str(name1).lower(), str(name2).lower()).ratio()
        if score >= threshold:
            df.at[i, "DuplicateOf"] = name2
            df.at[i, "Similarity"] = f"{round(score * 100, 2)}%"
            df.at[j, "DuplicateOf"] = name1
            df.at[j, "Similarity"] = f"{round(score * 100, 2)}%"

# ✅ Output result
df.to_csv("qbo_COA_duplicates_marked.csv", index=False, encoding="utf-8-sig")
print("✅ Duplicate detection complete. File saved as COA_duplicates_marked.csv")
