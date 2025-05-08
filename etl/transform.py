import pandas as pd

def transform(input_path: str, output_path: str):
    print("🔹 Transforming data...")
    df = pd.read_csv(input_path)
    df['Nama'] = df['Nama'].str.upper()
    df['Jumlah (Rp)'] = df['Jumlah (Rp)'] * 1.1
    df.to_csv(output_path, index=False)
    print("✅ Transformation completed.")
