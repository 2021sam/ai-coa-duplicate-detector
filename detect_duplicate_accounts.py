import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the IIF file, skipping header noise lines
with open("COA.csv", "r", encoding="utf-8-sig") as f:
    lines = [line.strip() for line in f if line.startswith("ACCNT,")]

# Extract header fields from the !ACCNT line manually
header = [
    "TYPE", "NAME", "REFNUM", "TIMESTAMP", "ACCNTTYPE", "OBAMOUNT", "DESC", 
    "ACCNUM", "SCD", "BANKNUM", "EXTRA", "HIDDEN", "DELCOUNT", "USEID"
]

# Load the cleaned ACCNT lines into a DataFrame
from io import StringIO
data_clean = "\n".join(lines).replace("ACCNT,", "")
df = pd.read_csv(StringIO(data_clean), names=header[1:])  # skip "TYPE"

# Combine fields for similarity comparison
df["combined"] = df.apply(lambda row: " | ".join([
    str(row["NAME"]), str(row["ACCNUM"]), str(row["DESC"]), str(row["ACCNTTYPE"])
]), axis=1)

# Load the transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df["combined"].tolist(), convert_to_tensor=False)

# Compute similarity matrix
similarity_matrix = cosine_similarity(embeddings)

# Detect duplicates with a threshold
threshold = 0.95
duplicates = []
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        if similarity_matrix[i][j] > threshold:
            duplicates.append((
                df.iloc[i]["NAME"],
                df.iloc[j]["NAME"],
                round(similarity_matrix[i][j], 3)
            ))

# Sort duplicates by similarity score (descending)
duplicates_sorted = sorted(duplicates, key=lambda x: x[2], reverse=True)

# Output sorted duplicates
if duplicates_sorted:
    print("⚠️ Potential Duplicate Accounts Found (Sorted by Similarity):\n")
    for name1, name2, score in duplicates_sorted:
        print(f"- {name1} <--> {name2} | Similarity: {score}")
else:
    print("✅ No duplicate accounts detected above the threshold.")
