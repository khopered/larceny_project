#!/usr/bin/env python
# coding: utf-8

# ## Project: Food Deserts Influence Larceny Rates

# We are predicting whether or not a community is at risk for higher rates of larceny based on the amount of food deserts per population.

# import starter packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('crimedata2.csv') # read csv into pandas

print(df.describe()) # count, max, min, std, mean

# Replace '?' with NaN
df.replace('?', np.nan, inplace=True)

print(df.isna().sum()) # now we can get the sum of all null values in each column

# Viewing all columns with their datatypes as a list of tuples
data_types = [(col, df[col].dtype) for col in df.columns]

# Print the list of column names with their datatypes
for col, dtype in data_types:
    print(f"{col}: {dtype}")

# List of columns to convert to numeric
columns_to_convert = [
    'rapes', 'rapesPerPop', 'robberies', 'robbbPerPop', 'assaults', 'assaultPerPop', 
    'burglaries', 'burglPerPop', 'larcenies', 'larcPerPop', 'autoTheft', 'autoTheftPerPop', 
    'arsons', 'arsonsPerPop', 'ViolentCrimesPerPop', 'nonViolPerPop'
]

# Convert these columns to numeric, forcing invalid values to NaN
df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric)

# correlated variables to target variable, I did 25 just to see as many as I could
correlation_matrix = df.corr(numeric_only=True)
correlation_with_target = correlation_matrix['larcPerPop'].sort_values(ascending=False)
print(correlation_with_target.head(25))

