def biggest_vertebrate(animals, weights, vertebrates):
	if(len(animals) == 0 or len(vertebrates) == 0):#if list is empty return None
		return None
	greatest_weight = 0
	greatest_animal_weight = ""
	for i in range(len(animals)):
		for j in range(len(vertebrates)):
			if(vertebrates[j] == animals[i]):#finds animals that exist in the vertebrates list
				if(weights[i] > greatest_weight):
					greatest_animal_weight = animals[i]
					greatest_weight = weights[i]
				break
	if(greatest_weight == 0):
		return None
	else:
		return greatest_animal_weight 
				
def within_weight(animals, weights, weightLimit):
	a_w_w = [] # a_w_w == animals_within_weightLimit
	for i in range(len(animals)):
		if(weights[i] <= weightLimit):#if weight of an animal is less than or equal to weightLimit it will append the animal's name to the array
			a_w_w.append(animals[i])
	return a_w_w
		


def any_adjacent_vertebrates(animals, vertebrates):
	real_vert = False
	for i in range(len(animals)-1):
		for j in range(len(vertebrates)):
			if(animals[i] == vertebrates[j]):#if vertebrate is an animal then set real_vert to true
				real_vert = True
				break
		if(real_vert == True):
			real_vert = False
			for j in range(len(vertebrates)):
				if(animals[i+1] == vertebrates[j]):
					return True
	return False

def count_weights(weight_list):
	counter = 0
	for i in range(len(weight_list)-1):
		for j in range(i+1, len(weight_list)):
			value = weight_list[i] + weight_list[j]
			for k in range(len(weight_list)):
				if(weight_list[k] == value):
					counter += 1
					break
	return counter
