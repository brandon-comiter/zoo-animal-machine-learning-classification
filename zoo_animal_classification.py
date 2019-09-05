import pandas as pd
import numpy as np
import random
from collections import Counter

# incorperates a basic k-nearest neighbors
# machine learning algorithm
test_size = 0.2

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
	# df.drop(['catsize'], 1, inplace= True)
	return df

def new_animal():
	animal_traits = []
	animal_name = ''


	print("What is the name of the species?")
	animal_name = input().lower()

	#Questions  (1) 
	print('Do they have hair?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or No.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	print(animal_traits)
	#2
	print('Do they have feathers?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or No.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#3
	print('Does a', animal_name,'lay eggs?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or No.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#4
	print('Do they produce milk for their offspring?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or No.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#5
	print('Is a', animal_name, 'able to fly?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or No.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#6
	print('Is this species found in an aquatic environment?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or No.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#7
	print('Is a', animal_name,'a predator?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or No.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
		print('wat')
	else:
		animal_traits.append(0)
	#8
	print('Do they have teeth?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or No.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#9
	print('Do they have backbones?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or NO.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#10
	print('Is a', animal_name, 'venomous?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or NO.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#11
	print('Do they have fins?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or NO.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#12
	print('Does a', animal_name, 'breath oxygen?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or NO.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#13
	print('How many legs does a', animal_name, 'have\nset of values: {0,2,4,5,6,8}?')
	ans = int(input())
	while (ans % 2 == 1 or ans > 8):
		print('Invalid Answer\nType one of the numbers(listed below):\n{0,2,4,5,6,8}')
		ans = int(input())
	animal_traits.append(ans)
	#14
	print('Do they have tails?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or NO.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#15
	print('Is this animal domesticated?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or NO.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)
	#16
	print('Is a', animal_name,'just as big or bigger than a cat?')
	print('Type: yes or no!')
	ans = input().lower()
	while (ans is 'yes' or ans is 'no'):
		print('Invalid Answer\nType: Yes or NO.')
		ans = input().lower()
	if ans == 'yes':
		animal_traits.append(1)
	else:
		animal_traits.append(0)

	print('Answers Chosen:', animal_traits)
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

print("\n\nNote to user:\nThis is a toy [Machine Learning] program.")
print("The data set used in this example is small,\nand the features are loosly related to the classification.")
print("Additionally the data set contains only 3 amphibians which isn't ideal\n\n\n")

animal_traits, animal_name = new_animal()
# animal_traits = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 4, 1, 0, 1]

accuracy, train_set = get_accuracy()
print('The system guesses with an accuracy of', accuracy)
print('The animal you have described is a')


result = k_nearest_neighbors(train_set, animal_traits)

if (result == 1):
	print('Mammal: (Classification #', result,')')
elif (result == 2):
	print('Bird: (Classification #', result,')')
elif (result == 3):
	print('Reptile: (Classification #', result,')')
elif (result == 4):
	print('Fish: (Classification #', result,')')
elif (result == 5):
	print('Amphibian: (Classification #', result,')')
elif (result == 6):
	print('Insect or Arachnid: (Classification #', result,')')
elif (result == 7):
	print('Crustation: (Classification #', result,')')

