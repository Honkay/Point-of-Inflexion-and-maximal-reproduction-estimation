# CAMEROON  DATA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import datetime
import time


sns.set(rc = {"figure.figsize" : (8, 6)})
data = pd.read_csv('CAMEROON.csv', delimiter=';', skiprows=0, low_memory=False)
data.head()
data.info()
data.describe()
data.isnull().sum()
#correlation between the values
corr = data.corr()
plt.figure(figsize=(10, 8))

ax = sns.heatmap(corr, vmin = -1, vmax = 1, annot = True)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.show()
corr
# Pair Plot correlation between all attributes
sns.pairplot(data)
#plotting the data distribution
# KERNEL DISTRIBUTION ESTIMATION PLOT
#Kdeplot is a Kernel Distribution Estimation Plot which depicts the probability density function of the continuous or non-parametric data variables i.e. we can plot for the univariate or multiple variables altogether
plt.figure(figsize=(10, 8))
for i in range(14):
    plt.subplot(4, 4, i+1)
    sns.kdeplot(data.iloc[:,i+1], shade=True)
    plt.title(data.columns[i+1])
plt.tight_layout()
plt.show()
#Histograms and KDE combined
plt.figure(figsize=(10, 8))
for i in range(12):
    plt.subplot(4, 4, i+1)
    sns.boxplot(data.iloc[:,i+1])
    plt.title(data.columns[i+1])
plt.tight_layout()
plt.show()
#KDE 
plt.figure(figsize=(10, 8))
for i in range(12):
    plt.subplot(4, 4, i+1)
    sns.kdeplot(data.iloc[:,i+1])
    plt.title(data.columns[i+1])
plt.tight_layout()
plt.show()
# VIOLIN PLOT
plt.figure(figsize=(10, 8))
for i in range(12):
    plt.subplot(4, 4, i+1)
    sns.violinplot(data.iloc[:,i+1],palette=["lightblue", "lightpink"])
    plt.title(data.columns[i+1])
plt.tight_layout()
plt.show()
#plotting the data distribution
#EMPRICAL CUMMULATIVE DISTRIBUTION FUNCTIONS PLOT
#ecdfplot An ECDF represents the proportion or count of observations falling below each unique value in a dataset. Compared to a histogram or density plot, it has the advantage that each observation is visualized directly, meaning that there are no binning or smoothing parameters that need to be adjusted. It also aids direct comparisons between multiple distributions. A downside is that the relationship between the appearance of the plot and the basic properties of the distribution (such as its central tendency, variance, and the presence of any bimodality) may not be as intuitive.
plt.figure(figsize=(10, 8))
for i in range(12):
    plt.subplot(4, 4, i+1)
    sns.ecdfplot(data.iloc[:,i+1])
    plt.title(data.columns[i+1])
plt.tight_layout()
plt.show()