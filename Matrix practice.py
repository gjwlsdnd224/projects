def increment_attendance(seating, locations):
	for i in locations:
		(x,y) = i
		seating[x][y] += 1

def drop_lowest(scores, drop_number):
	for i in range(len(scores)):
		sort = sorted(scores[i]) # puts scores from least to greatest
		for j in range(drop_number[i]):
			scores[i].remove(sort[j]) # will remove whatever place the drop_number is at in scores

def organize_grades(grades, assignment_types, max_possible):
	gbook = {'zy':[], 'lab':[], 'pa':[], 'mid1':[], 'mid2':[], 'final':[], }
	for i in range(len(grades)):
		gbook[assignment_types[i]].append(grades[i]/max_possible[i])
	return gbook
	
def gbook_averages(gbook):
	average = {}
	for value,list1 in gbook.items():
		if len(list1) != 0:
			average[value] = sum(list1)/len(list1)	
		elif len(list1) == 0:
			average[value] = 0.0	
	return average
	
def course_grade(gbook, weights, replace):
	gbook2=gbook.copy()# makes a copy of gbook
	count = 0 
	for a1,a2 in replace.items():
		if gbook[a1] > gbook[a2]:
			gbook2[a2] = gbook[a1]
	for k in gbook2:
		count += gbook2[k] * weights[k]
	return count
