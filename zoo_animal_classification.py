import pandas as pd
import numpy as np
import random
from collections import Counter

test_size = 0.3

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

def new_animal():
	animal_traits = []
	animal_name = ''

	
	print("What is the animals species?")
	animal_name = input()

	#1
	print('Does it have hair?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	print(animal_traits)

	#2
	print('Does it have feathers?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#3
	print('Does ', animal_name,' lay eggs?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#4
	print('Does it produce milk for its offspring?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#5
	print('Is ', animal_name, ' airborne?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	print(animal_traits)
	#6
	print('Is the animal found in an aquatic environment?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#7
	print('Is the animal a predator?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
		print('wat')
	else:
		animal_traits.append(0)
	#8
	print('Does it have teeth?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#9
	print('Does it have a backbone?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#10
	print('Is it venomous?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	print(animal_traits)

	#11
	print('Does it have fins?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	print(animal_traits)
	#12
	print('Does it breath oxygen?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#13
	print('How many legs does it have\nset of values: {0,2,4,5,6,8}?')
	ans = int(input())	
	while (ans % 2 == 1 or ans > 8):	
		print('Invalid Answer\nType one of the numbers(listed below):\n{0,2,4,5,6,8}')
		ans = int(input())
	animal_traits.append(ans)
	#14
	print('Does it have a tail?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#15
	print('Does it have a domestic?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):	
		print('Invalid Answer\nType: Yes or NO.')
		ans = input.lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)

	
	print(animal_traits)
	return animal_traits, animal_name

def get_accuracy():
	df = read_in_zoo_data()
	full_data = df.astype(int).values.tolist()
	random.shuffle(full_data)

	train_set = {1: [], 2: [], 3: [], 4: []
			,5: [], 6: [], 7: []}
	test_set = {1: [], 2: [], 3: [], 4: []
			,5: [], 6: [], 7: []}

	train_data = full_data[ :-int(test_size * len(full_data))]
	test_data = full_data[-int(test_size * len(full_data)):]

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
	return accuracy, train_set
	
# animal_traits, animal_name = new_animal()
# animal_traits = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]

accuracy, train_set = get_accuracy() 
print('The system guesses with an accuracy of ', accuracy, ' that \nthe animal you have described is!')
print('A type (',k_nearest_neighbors(train_set, animal_traits), ')')
