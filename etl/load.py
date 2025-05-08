import pandas as pd

def load(input_path: str, output_path: str):
    print("🔹 Loading data...")
    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)
    print("✅ Load completed.")
