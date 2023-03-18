def to_do(is_weekend, is_rainy, is_cold):
	if is_weekend == True:
		if is_rainy == False:
			if is_cold == False:
				result = "Go for a hike"
			else:
				result = "Go skiing"
		else:
			result = "Stay inside and watch movies"
	elif is_weekend == False:
		if is_rainy == False:
			if is_cold == False:
				result = "Go to the park"
			else:
				result = "Stay inside and read a book"
		else:
			result = "Go to the mall"
	return result
	
def priority_level(amount):
	if amount >= 10000:
		result = 1
	elif amount >= 7500 and amount <= 10000:
		result = 2
	elif amount >= 5000 and amount < 7500:
		result = 3
	elif amount < 5000 and str(amount)[3] == "5":
		result = 4
	elif amount < 5000 and str(amount)[3] == "3":
		result = 4
	else:
		result = 5
	
	return result

def categorize(item_price, item_units):
    if item_price < 10 and item_units < 10:
        result = "Low-priced"
    elif 10 <= item_price <= 20 and item_units < 20:
        result = "Mid-priced"
    elif item_price > 20 and item_units < 30:
        result = "High-priced"
    elif item_price > 20 and item_units >= 30:
        result = "Premium"
    else:
        result = "Other"
        
    return result


def ticket_price(customer_age, day_of_week):
    if customer_age < 10:
        if day_of_week == "Monday":
            result = 5 * .80
        elif day_of_week == "Wednesday":
            result = 5 * .90
        else:
            result = 5
    elif 10 <= customer_age <= 17:
        if day_of_week == "Monday":
            result = 8 * .80
        else:
            result = 8
    elif 18 <= customer_age <= 59:
        if day_of_week == "Monday":
            result = 10 * .80
        else:
            result = 10
    elif customer_age >= 60:
        if day_of_week == "Monday":
            result = 7 * .80
        elif day_of_week == "Tuesday":
            result = 7 * .75
        else:
            result = 7
    
    return result
