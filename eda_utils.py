import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
from ydata_profiling import ProfileReport

def generate_profile(df):
    return ProfileReport(df, title="Pandas Profiling Report", explorative=True)
    
#Handle missing values
def clean_data(df, method="do_nothing"):
    if method == "drop":
        return df.dropna()
    elif method == "mean":
        return df.fillna(df.mean(numeric_only=True))
    return df

#Generate descriptive stats
def describe_data(df):
    return df.describe()

#Generate plotly or seaborn plots
def generate_plot(df, plot_type, x=None, y=None, color=None):
    if plot_type == "histogram":
        return px.histogram(df, x=x, y=y, nbins=30, title=f"Histogram of {x}")
    elif plot_type == "boxplot":
        return px.box(df, x=x, y=y, title=f"Boxplot of {y} by {x}")    
    elif plot_type == "scatter":
        return px.scatter(df, x=x, y=y, color=color, title=f"Scatterplot of {y} vs {x}")
    elif plot_type == "heatmap":
        corr = df.select_dtypes(include=['float64', 'int64']).corr()
        fig, ax = plt.subplots() 
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        return fig
    elif plot_type == "swarm":
        fig, ax = plt.subplots()
        sns.swarmplot(data=df, x=x, y=y, ax=ax)
        return fig      