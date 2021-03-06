import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer

dataset = pd.read_csv('/Users/JohnMB2011/Downloads/Machine_Learning_Code_Datasets/Part1_Data_Preprocessing/Section2/Python/Data.csv')
# include all rows and all columns except the last column
x = dataset.iloc[:, :-1].values
# include all rows and the last column
y = dataset.iloc[:, -1].values

print(x)
print(y)

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

print(x)