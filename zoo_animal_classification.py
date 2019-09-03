import pandas as pd
import numpy as np
import random
from collections import Counter

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

def read_in_zoo_data():
	# Reads data into dataframe and applies headers to the data
	df = pd.read_csv('zoo.data', header= None)
	df.columns = ['Name', 'hair' , 'feathers', 'eggs', 'milk', 'aquatic', 'airborne',
				'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins',
				'legs#', 'tail', 'domestic', 'catsize', 'classification']

	# Name(not a predictor of classification) 
	# catsized(ambigous)
	df.drop(['Name'], 1, inplace= True)
	df.drop(['catsize'], 1, inplace= True)
	return df




animal_traits = []

print("What is the animals name?")
animal_name = input()
print("Does it have hair")
print("1: YES 0: NO")
animal_traits.append(int(input()))
print(animal_traits)




df = read_in_zoo_data()

full_data = df.astype(float).values.tolist()
random.shuffle(full_data)
# print(full_data)

test_size = 0.3

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
		vote = k_nearest_neighbors(train_set, data, k=3)
		if (group == vote):
			correct+=1
		total+=1

accuracy = correct/total
print(type(full_data))
print(type(test_set))
print(accuracy)
print(k_nearest_neighbors(train_set, animal_traits))
