#! /usr/bin/env python3

"""
Iris Plot Script

This script reads the iris dataset, performs linear regression
for each species, and generates scatter plots with regression lines.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def plot_species(dataframe, species):
    """
    Create regression plot for a given species
    """
    species_df = dataframe[dataframe.species == species]

    x = species_df.petal_length_cm
    y = species_df.sepal_length_cm

    reg = stats.linregress(x, y)

    plt.figure()
    plt.scatter(x, y, label=f"{species} data")
    plt.plot(x, reg.slope * x + reg.intercept, color="orange")

    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.title(species)
    plt.legend()

    plt.savefig(f"{species}.png")
    plt.close()
 
def main():
    dataframe = pd.read_csv("iris.csv")

    for species in dataframe.species.unique():
        plot_species(dataframe, species)


if __name__ == "__main__":
    main()
