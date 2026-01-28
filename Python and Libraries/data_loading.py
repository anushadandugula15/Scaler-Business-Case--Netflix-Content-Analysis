import pandas as pd
from config import DATA_PATH

def load_data(path=DATA_PATH):
    """Load Netflix dataset from CSV"""
    return pd.read_csv(path)

if __name__ == "__main__":
    df = load_data()
    print(f"Dataset loaded with shape: {df.shape}")
