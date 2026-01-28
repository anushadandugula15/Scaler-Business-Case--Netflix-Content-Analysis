def explode_multivalued_columns(df):
    """Split and explode multi-valued columns"""
    df['listed_in'] = df['listed_in'].str.split(',')
    df['country'] = df['country'].str.split(',')
    df['director'] = df['director'].str.split(',')

    df = (
        df.explode('listed_in')
          .explode('country')
          .explode('director')
    )

    df['listed_in'] = df['listed_in'].str.strip()
    df['country'] = df['country'].str.strip()
    df['director'] = df['director'].str.strip()

    return df
