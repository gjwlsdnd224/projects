print("Welcome to Mael's Calculator")
#User input data for coffee pounds
A_Pounds = int(input("Total Coffee A Pounds: "))
B_Pounds = int(input("Total Coffee B Pounds: "))
C_Pounds = int(input("Total Coffee C Pounds: "))
#User input data for price/Kg
Coffee_A = float(input("Coffee A Price/Kg: "))
Coffee_B = float(input("Coffee B Price/Kg: "))
Coffee_C = float(input("Coffee C Price/Kg: "))
#changes pounds to kg
def p_to_k(pounds):
	kg = pounds/2.2046
	return kg	
A_kg = p_to_k(A_Pounds)
B_kg = p_to_k(B_Pounds)
C_kg = p_to_k(C_Pounds)

#calculates total amount for selling each coffee
Sell_A = round(A_kg * Coffee_A,2)
Sell_B = round(B_kg * Coffee_B,2)
Sell_C = round(C_kg * Coffee_C,2)

A = A_kg * Coffee_A
B = B_kg * Coffee_B
C = C_kg * Coffee_C
print("Selling all of Coffee A makes: $" + str(Sell_A))
print("Selling all of Coffee B makes: $" + str(Sell_B))
print("Selling all of Coffee C makes: $" + str(Sell_C))
total = round(A + B + C,2)
print("Selling all of the Coffee makes:" + " $" + str(total))

print("***Valentine's Day Special***")
orders = int(input("Enter total orders: "))

#Red Velvet Mocha
rvm = (2 * Coffee_A + Coffee_B)/2.2046 * orders
r_tax = rvm * .1
rvm = rvm + r_tax
rvm = round(rvm,2)
print("Charge " + "$" + str(rvm) + " for Red Velvet Mocha")
rvm_a = round(2 * orders/2.2046,2)
rvm_b = round(orders/2.2046,2)
print("Need " + str(rvm_a)+ "kg of Coffee A " + "and " + str(rvm_b) + "kg " + "of Coffee B")

#Valentine's Day Frap
vdf = (2.5 * Coffee_B + 1.5 * Coffee_C)/2.2046 * orders
v_tax = vdf * .1
vdf = round(vdf + v_tax,2)
print("Charge " + "$" + str(vdf) + " for Valentine's Day Frapp")
vdf_b = round(2.5 * orders/2.2046,2)
vdf_c = round(1.5 * orders/2.2046,2)
print("Need " + str(vdf_b)+ "kg of Coffee B " + "and " + str(vdf_c) + "kg " + "of Coffee C")

#Lover's Spice
ls = (.45 * Coffee_A + 2.16 * Coffee_C)/2.2046 * orders
l_tax = ls * .1
ls = round(ls + l_tax,2)
print("Charge " + "$" + str(ls) + " for Lover's Spice")
ls_a = round(.45 * orders/2.2046,2)
ls_c = round(2.16 * orders/2.2046,2)
print("Need " + str(ls_a)+ "kg of Coffee A " + "and " + str(ls_c) + "kg " + "of Coffee C")

#Cups
total_cups = orders 
total_packages = total_cups // 50
additional_cups = total_cups % 50
print("Need " + str(total_packages) + " packages of cups and " + str(additional_cups) + " additional cup(s)")