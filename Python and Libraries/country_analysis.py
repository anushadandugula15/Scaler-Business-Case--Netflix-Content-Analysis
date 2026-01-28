def top_countries(df, n=10):
    """Return top N countries by content volume"""
    return (
        df['country']
        .value_counts()
        .head(n)
    )

def content_by_country_and_type(df, countries):
    """Compare Movies vs TV Shows for selected countries"""
    return (
        df[df['country'].isin(countries)]
        .groupby(['country', 'type'])
        .size()
        .reset_index(name='count')
    )
