import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
                color='blue', label='Original Data')

    # First line of best fit (all data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = range(1880, 2051)
    plt.plot(years1, res1.slope*years1 + res1.intercept, 
             'r', label='Best Fit (1880-2050)')

    # Second line of best fit (2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years2 = range(2000, 2051)
    plt.plot(years2, res2.slope*years2 + res2.intercept, 
             'green', label='Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
