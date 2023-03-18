def spectral_color(wavelength):
	if wavelength < 380:
		return "ultraviolet"
	elif 380 <= wavelength and wavelength < 450:
		return "violet"
	elif 450 <= wavelength and wavelength < 485:
		return "blue"
	elif 485 <= wavelength and wavelength < 500:
		return "cyan"
	elif 500 <= wavelength and wavelength < 565:
		return "green"
	elif 565 <= wavelength and wavelength < 590:
		return "yellow"
	elif 590 <= wavelength and wavelength < 625:
		return "orange"
	elif 625 <= wavelength and wavelength < 750:
		return "red"
	else:
		return "infrared"

def robot_actions(side_sensor, front_sensor, dirt_sensor):
	if dirt_sensor == "dirt":
		return "vacuum"
	if dirt_sensor == "clear":
		if side_sensor == "wall" and front_sensor == "clear":
			return "forward"
		elif front_sensor == "wall":
			return "turn"
	#robot doesn't turn off because everything is false.
	if dirt_sensor == "clear":
		if side_sensor == "clear":
			if front_sensor == "clear":
				return "stop"

		
	

def bad_broker(price, prev_price):
	#if stock is 50% more than prev_price buy
	if price/prev_price >= 1.5:
		return "BUY"
	#if stock is less than 50% than prev_price hold
	if price/prev_price <= 0.5:
		return "HOLD"
	else:
		return "SELL"
	
