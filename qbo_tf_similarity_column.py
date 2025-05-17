import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity





# ✅ Load data
# Load CSV, skipping metadata rows to get proper headers
df = pd.read_csv("Paint Productions, Inc._Account List.csv", skiprows=2)

# Normalize column names: strip spaces and convert to lowercase
df.columns = df.columns.str.strip().str.lower()

# Print normalized columns to confirm
print("Normalized Columns:", df.columns.tolist())

# Filter rows where 'full name' column is not empty or NaN
df = df[df["full name"].notna()].reset_index(drop=True)



# ✅ Load USE model
model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
use_model = hub.load(model_url)

# ✅ TensorFlow tensor input
names = df["NAME"].astype(str).tolist()
name_embeddings = use_model(tf.constant(names))  # <-- Explicit use of tf.constant()

# ✅ Compute cosine similarity
similarity_matrix = cosine_similarity(name_embeddings.numpy())

# ✅ Threshold for duplicates
threshold = 0.85
df["DuplicateOf"] = ""
df["Similarity"] = ""

# ✅ Find duplicates
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        score = similarity_matrix[i][j]
        if score >= threshold:
            df.at[i, "DuplicateOf"] = df.at[j, "NAME"]
            df.at[i, "Similarity"] = f"{score:.2%}"
            df.at[j, "DuplicateOf"] = df.at[i, "NAME"]
            df.at[j, "Similarity"] = f"{score:.2%}"

# ✅ Save result
df.to_csv("qbo_tf_COA_tensorflow_duplicates.csv", index=False)
print("✅ TensorFlow-based duplicate detection complete.")
