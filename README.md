# ai-coa-duplicate-detector
A TensorFlow-powered tool to identify duplicate or highly similar Chart of Accounts (COA) entries for accounting systems like QuickBooks.


# COA Duplicate Detector 🧠

A lightweight AI-powered tool for identifying duplicate or highly similar Chart of Accounts (COA) entries in QuickBooks or similar accounting systems.

## 🔍 Purpose

This project uses TensorFlow (or other ML methods) to analyze COA records and flag potential duplicates based on similarity in account names, types, and hierarchy. This is particularly useful for:

- Detecting duplicates across departments like Repair Centers
- Auditing and standardizing COA data
- Confirming data integrity after migrations or bulk uploads

## 📁 Features

- Uses natural language embeddings to compare account names
- Supports CSV or Excel input
- Distinguishes between mapped and unmapped accounts
- Works with 4-digit vs 5-digit numbering schemes

## 🧰 Requirements

- Python 3.8+
- TensorFlow
- Pandas
- scikit-learn

Install dependencies:

```bash
pip install -r requirements.txt
