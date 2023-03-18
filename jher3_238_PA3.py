def break_time(hours_worn, last_break):	

	result = 0
	j = hours_worn
	while j % last_break > 0:
		j = int(j / last_break)	
		result+= 1
	
	return result


def how_many_uruks(strength_values, init_fund_needed):
	
	budget = 0
	result = 0
	for value in strength_values:
		if value == 0:
			budget += value
		elif value % 2 == 0:
			budget *= value
		elif value % 2 == 1:
			budget += value
	while budget > init_fund_needed:
		budget -= init_fund_needed
		init_fund_needed += 1 # will add one init fund because it will take one more fund to make another uruk
		result += 1 # will add how many uruks I was able to make while running through the loop
				
	return result


def years_to_rule(n1, n2, n3):		

	result = 0
	for i in range(1,n1+1):
		for j in range(1,n2+1):
			result += i*j // n3
	return result


def lotr_popularity(char_list):
	
	result = ""
	
	return result
