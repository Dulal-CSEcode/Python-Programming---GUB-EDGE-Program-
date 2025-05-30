# -*- coding: utf-8 -*-
"""Problem 4: You generate a NumPy array containing 10,000 real-valued random numbers representing measurements from a scientific experiment. Your goal is to analyze the statistical properties of this dataset..ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xPdPg_OH9yoF7UBSM8gI3uLDS2ZsMAL4

# **Problem 4: You generate a NumPy array containing 10,000 real-valued random numbers representing measurements from a scientific experiment. Your goal is to analyze the statistical properties of this dataset.**
"""

import numpy as np


np.random.seed(42)
data = np.random.randn(10000)


mean_value = np.mean(data)
median_value = np.median(data)
std_dev = np.std(data)



min_value = np.min(data)
max_value = np.max(data)



count_above_mean = np.sum(data > mean_value)



normalized_data = (data - min_value) / (max_value - min_value)



print(f"Mean: {mean_value}\n")
print(f"Median: {median_value}\n")
print(f"Standard Deviation: {std_dev}\n")
print(f"Minimum Value: {min_value}\n")
print(f"Maximum Value: {max_value}\n")
print(f"Number of values greater than the mean: {count_above_mean}\n")
print(f"First 10 normalized values: {normalized_data[:10]}")