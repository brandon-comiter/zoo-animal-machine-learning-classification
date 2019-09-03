import pandas as pd
import numpy as np
from sklearn import neighbors, preprocessing 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style
from math import sqrt
from collections import Counter
style.use('fivethirtyeight')



def k_nearest_neighbors(dataset, predict):
    pass

df = pd.read_csv('zoo.data', header= None)
df.columns = ['Name', 'hair' , 'feathers', 'eggs', 'milk', 'aquatic',
 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs',
  'legs#', 'tail', 'domestic', 'catsize', 'classification']

print(df)

