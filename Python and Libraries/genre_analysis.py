def top_genres(df, n=5):
    """Return top N genres by count"""
    return (
        df['listed_in']
        .value_counts()
        .head(n)
    )
