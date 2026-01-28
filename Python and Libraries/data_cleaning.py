import pandas as pd

def clean_data(df):
    """Handle missing values and data types"""
    df[['type', 'title', 'cast']] = df[['type', 'title', 'cast']].fillna('NA')
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
    return df
