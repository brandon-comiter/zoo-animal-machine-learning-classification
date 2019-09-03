import pandas as pd
import numpy as np
import random
# from sklearn import neighbors, preprocessing 
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# from matplotlib import style
# from math import sqrt
from collections import Counter
# style.use('fivethirtyeight')

# k-nearest neighbors function
def k_nearest_neighbors(dataset, predict, k= 5):
	distances = []
	for group in dataset:
		for feature in dataset[group]:
			euclidean_distance = np.linalg.norm(np.array(feature) - np.array(predict))
			distances.append([euclidean_distance, group])
			

	leanings = [i[1] for i in sorted(distances)[:k]]
	leaning_result = Counter(leanings).most_common(1)[0][0]
	
	return leaning_result

# Reads data into dataframe and applies headers to the data
df = pd.read_csv('zoo.data', header= None)
df.columns = ['Name', 'hair' , 'feathers', 'eggs', 'milk', 'aquatic',
			'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs',
			'legs#', 'tail', 'domestic', 'catsize', 'classification']

d = [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 4, 0, 0]

# Name(not a predictor of classification) 
# catsized(ambigous)

df.drop(['Name'], 1, inplace= True)
df.drop(['catsize'], 1, inplace= True)


full_data = df.astype(float).values.tolist()
random.shuffle(full_data)
# print(full_data)

test_size = 0.2

train_set = {1: [], 2: [], 3: [], 4: []
			,5: [], 6: [], 7: []}
test_set = {1: [], 2: [], 3: [], 4: []
		   ,5: [], 6: [], 7: []}

train_data = full_data[ :-int(test_size * len(full_data))]
test_data = full_data[-int(test_size * len(full_data)): ]


for i in train_data:
	train_set[i[-1]].append(i[:-1])
for i in test_data:
	test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
	for data in test_set[group]:
		vote = k_nearest_neighbors(train_set, data, k=5)
		if (group == vote):
			correct+=1
		total+=1

accuracy = correct/total

print(accuracy)

# for i in test_dataset:
# 	test_set[i[-1]].append(i[:-1])

# k_nearest_neighbors(dataset, d)
