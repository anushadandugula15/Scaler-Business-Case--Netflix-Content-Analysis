def rating_distribution(df):
    """Distribution of content ratings"""
    return df['rating'].value_counts()

def rating_by_type(df):
    """Ratings split by Movies and TV Shows"""
    return (
        df.groupby(['rating', 'type'])
          .size()
          .reset_index(name='count')
    )
