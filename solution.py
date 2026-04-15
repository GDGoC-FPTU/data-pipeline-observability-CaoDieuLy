"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-XXXX  (<-- Thay XXXX bang ma so cua ban)
Name: Your Name Here

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import os
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.

    Goi y:
       - Dung json.load() de doc file JSON
       - Xu ly truong hop file khong ton tai (FileNotFoundError)

    Returns:
        list: Danh sach cac records (dictionaries)
    """
    print(f"Extracting data from {file_path}...")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {file_path}: {e}")
        return []

    if not isinstance(data, list):
        print("Extracted JSON is not a list of records. Returning empty list.")
        return []

    print(f"Extraction complete. Records: {len(data)}")
    return data


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.

    Quy tac validation:
       - Price phai > 0 (loai bo gia am hoac bang 0)
       - Category khong duoc rong

    Goi y:
       - Dung record.get('price', 0) de lay gia
       - Dung record.get('category') de kiem tra category
       - In ra so luong record hop le va khong hop le

    Returns:
        list: Danh sach cac records hop le
    """
    valid_records = []
    error_count = 0

    if not data:
        print("Validation summary: 0 valid, 0 errors")
        print("Validation complete. Valid: 0, Errors: 0")
        return []

    for record in data:
        if not isinstance(record, dict):
            error_count += 1
            continue

        price = record.get('price', 0)
        category = record.get('category')

        try:
            price_value = float(price)
        except (TypeError, ValueError):
            error_count += 1
            continue

        if price_value <= 0:
            error_count += 1
            continue

        if category is None or str(category).strip() == "":
            error_count += 1
            continue

        normalized = dict(record)
        normalized['price'] = price_value
        normalized['category'] = str(category).strip()
        valid_records.append(normalized)

    print(f"Validation summary: {len(valid_records)} valid, {error_count} errors")
    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.

    Yeu cau:
       - Tinh discounted_price = price * 0.9 (giam 10%)
       - Chuan hoa category thanh Title Case (vi du: "electronics" -> "Electronics")
       - Them cot processed_at = timestamp hien tai

    Goi y:
       - Dung pd.DataFrame(data) de tao DataFrame
       - df['discounted_price'] = df['price'] * 0.9
       - df['category'] = df['category'].str.title()
       - df['processed_at'] = datetime.datetime.now().isoformat()

    Returns:
        pd.DataFrame: DataFrame da duoc transform
    """
    if not data:
        print("Transform skipped: no valid records.")
        return pd.DataFrame(columns=['price', 'category', 'discounted_price', 'processed_at'])

    df = pd.DataFrame(data)

    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
    else:
        df['price'] = 0.0

    df['discounted_price'] = df['price'] * 0.9
    if 'category' in df.columns:
        df['category'] = df['category'].astype(str).str.strip().str.title()
    else:
        df['category'] = ""
    df['processed_at'] = datetime.datetime.now().isoformat()

    print(f"Transform complete. Records: {len(df)}")
    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.

    Goi y:
       - df.to_csv(output_path, index=False)
    """
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    # 2. Validate (works even if raw_data is empty)
    clean_data = validate(raw_data)

    # 3. Transform
    final_df = transform(clean_data)

    # 4. Load
    if final_df is not None:
        load(final_df, OUTPUT_FILE)
        print(f"\nPipeline completed! {len(final_df)} records saved.")
    else:
        print("\nTransform returned None. Check your transform() function.")
