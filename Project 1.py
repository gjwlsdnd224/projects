print("Sage's Wedding Cake Price Calculator")

people = int(input("Total People Attending:"))
cake = people / 30
print(" ----------------------------------------")
#Cake A
print("Cake A")
costA = 15 * 15 + 12.50 # Formula for Cost baking time + hourly wage + Sage wage
print("Labor Cost:     \t$" + str(round(costA * cake,2)))
print("Cost to Make:   \t$" + str(round((costA + 35) * cake,2)))
print("Charge Customer: \t$" + str(round(((costA + 35) * 1.1) * cake,2)))
#Cake B
print("----------------------------------------")
print("Cake B")
costB = (14 * 15) + (12.50 * 2)
print("Labor Cost:     \t$" + str(round(costB * cake,2)))
print("Cost to Make:   \t$" + str(round((costB + 30) * cake,2))) 
print("Charge Customer: \t$" + str(round(((costB + 30) * 1.1) * cake,2)))
print("----------------------------------------")
#Cake C
print("Cake C") 
costC = (16 * 15) + (12.5 * 1.5)
print("Labor Cost:     \t$" + str(round(costC * cake,2)))
print("Cost to Make:   \t$" + str(round((costC + 40) * cake,2)))
print("Charge Customer: \t$" + str(round(((costC + 40) * 1.1) * cake,2)))