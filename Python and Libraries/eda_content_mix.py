import matplotlib.pyplot as plt
import seaborn as sns

def plot_movies_vs_tvshows(df):
    """Visualize Movies vs TV Shows"""
    sns.countplot(data=df, x='type')
    plt.title("Movies vs TV Shows on Netflix")
    plt.xlabel("Content Type")
    plt.ylabel("Count")
    plt.show()
