pennies = int(input("how many pennies will you like to enter?"))

dollars = pennies//100
pennies = pennies % 100
quarters = pennies//25
pennies = pennies % 25
dimes = pennies//10
pennies = pennies % 10
nickels = pennies//5
pennies = pennies % 5

print(("dollars") + str(dollars))
print(("quarters") + str(quarters))
print(("dimes") + str (dimes))
print(("nickels") + str (nickels))
print(("pennies") + str(pennies))s



