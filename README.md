# ai-coa-duplicate-detector

A lightweight AI-powered tool for identifying duplicate or highly similar Chart of Accounts (COA) entries in QuickBooks or similar accounting systems.

---

## 🔍 Purpose

This project uses TensorFlow (or other ML methods) to analyze COA records and flag potential duplicates based on similarity in account names, types, and hierarchy. This is particularly useful for:

- Detecting duplicates across departments like Repair Centers
- Auditing and standardizing COA data
- Confirming data integrity after migrations or bulk uploads

---

## 📜 Script Summary

### ✅ `similarity_sort.py`

**Purpose:**  
Analyzes a QuickBooks Chart of Accounts (COA) file (`COA.csv`) and identifies potentially **duplicate or similar account entries** based on text similarity.

**What it does:**
- Loads and parses the COA file.
- Computes pairwise similarity scores using fuzzy matching or embedding distances.
- Sorts and prints similar account pairs **in descending order of similarity**.

---

### ✅ `similarity_columns.py`

**Purpose:**  
Extends `similarity_sort.py` by producing a copy of the COA with **two additional helper columns** for human review.

**What it does:**
- Creates a copy of `COA.csv`.
- Adds:
  - `Most_Similar_To`: Closest matching account.
  - `Similarity_Score`: Their similarity percentage.
- Saves an annotated file for auditing, review, or manual cleanup.

---

## 📁 Features

- Uses natural language embeddings or fuzzy matching for comparison
- Supports CSV or Excel input
- Differentiates mapped vs unmapped accounts
- Compatible with 4-digit and 5-digit account numbering schemes

---

## 🧰 Requirements

- Python 3.8+
- TensorFlow
- pandas
- scikit-learn

Install dependencies:

```bash
pip install -r requirements.txt
