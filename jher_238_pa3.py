def sum_evens(n):
	sum1 = 0
	for i in range(n+1): #takes the n and increments up from 0
		if i % 2 == 0: #takes n and mods by 2 and checks if it's equal to 0
			sum1 += i
	return sum1

def is_deficit(n):
	sum1 = 0
	for i in range(1, n+1):
		#makes sure n is a factor by i and also checks that i doesn't equal n
		if n % i == 0 and i != n:
			sum1 += i
			if sum1 <= n:
				result = True
			else:
				result = False 
	return result


def list_deficits(bottom, top):
	lists = [] #creates an empty list
	for i in range(bottom, top+1):
		if is_deficit(i):
			lists.append(i) # adds i to new list called lists
	return lists

def hail_steps(n):
	num_steps = 0
	while n != 1:
		if n % 2 ==0:
			n = n // 2
		else:
			n = (n * 3) + 1
		num_steps += 1
	return num_steps

def keep_em(names, keepers):
	keep = []
	for i in range(len(names)):
		if keepers[i] == True:
			keep.append(names[i])
	return keep


def more_mults(lst1_bottom, lst1_top, lst2_bottom, lst2_top, factor):
	c1 = 0
	c2 = 0
	lst1 = []
	lst2 = []
	#creates two lists using range and appens to their respectful list
	for i in range(lst1_bottom,lst1_top+1):
		lst1.append(i)
	for i in range(lst2_bottom,lst2_top+1):
		lst2.append(i)
		
	#counts number of multiples
	for val in lst1:
		if val % factor == 0:
			c1 += 1
	for val in lst2:
		if val % factor == 0:
			c2 += 1
	
	#determines the winner based on who has more multiples if same shorter list wins
	if c1 > c2:
		winner = "List 1"
	elif c1 < c2:
		winner = "List 2"
	elif c1 == c2 and len(lst1) < len(lst2):
		winner = "List 1"
	elif c1 == c2 and len(lst1) > len(lst2):
		winner = "List 2"
	else:
		winner = "Tie"
	return winner
	
	