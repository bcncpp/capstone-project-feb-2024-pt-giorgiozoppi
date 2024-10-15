#!/usr/bin/env python3

import polars as pl

def convert_csv_to_parquet(csv_file, parquet_file):
    df = pl.read_csv(csv_file)
    df.write_parquet(parquet_file)

if __name__=="__main__":
    print("Converting CSV to Parquet...")
    csv_file = f"hotel_reviews.csv"
    parquet_file = f"hotel_reviews.parquet"
    convert_csv_to_parquet(csv_file, parquet_file)
