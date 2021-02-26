import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('/Users/JohnMB2011/Downloads/Machine_Learning_Code_Datasets/Part1_Data_Preprocessing/Section2/Python/Data.csv')
# include all rows and all columns except the last column
x = dataset.iloc[:, :-1].values
# include all rows and the last column
y = dataset.iloc[:, -1].values

print(x)
print(y)