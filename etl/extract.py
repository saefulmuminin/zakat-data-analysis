import pandas as pd

def extract(input_path: str, output_path: str):
    print("🔹 Extracting data...")
    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)
    print("✅ Extraction completed.")
