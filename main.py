from etl.extract import extract
from etl.transform import transform
from etl.load import load

# File paths
RAW_DATA = 'data/zakat.csv'
EXTRACTED = 'data/temp_extract.csv'
TRANSFORMED = 'data/temp_transform.csv'
CLEANED = 'data/clean_zakat.csv'

def main():
    extract(RAW_DATA, EXTRACTED)
    transform(EXTRACTED, TRANSFORMED)
    load(TRANSFORMED, CLEANED)
    print("ETL pipeline finished successfully.")

if __name__ == "__main__":
    main()
