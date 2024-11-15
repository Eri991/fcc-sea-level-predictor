import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    line1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(df['Year'].min(), 2050+1, 1))
    y1 = line1.intercept + x1 * line1.slope
    plt.plot(x1, y1)

    # Create second line of best fit
    df_2k = df[df['Year'] >= 2000]
    line2 = linregress(x=df_2k['Year'], y=df_2k['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(df_2k['Year'].min(), 2050+1, 1))
    y2 = line2.intercept + x2 * line2.slope
    plt.plot(x2, y2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()