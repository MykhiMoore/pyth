# DRY - Don't Repeat Yourself
# DRY - Don't Repeat Yourself
# DRY - Don't Repeat Yourself
# DRY - Don't Repeat Yourself

def directions():
    print("Turn Left Out Of Parking Lot. ")
    print("drive to stop light and turn left. ")
    print("Drive one mile through Canfield")
    print("Starbucks is across the street from Sheetz. ")
    print("Turn left into Starbucks")
    
number_of_people = int(input("How many people are asking for directions? "))

while number_of_people > 0:
   print(f"{number_of_people} - New Direction")
   directions()
   number_of_people = number_of_people - 1
print("Kankan")