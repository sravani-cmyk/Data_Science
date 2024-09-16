# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# 1...Write a program that asks user to enter a city name and it should tell which
#  country the city belongs to
# 
# 2.... Write a program that asks user to enter two cities and it tells you 
# if they both are in same country or not. For example if I enter mumbai
#  and chennai, it will print "Both cities are in India" but if I enter mumbai 
# and dhaka it should print "They don't belong to same country"
############### solution 1...... #####################
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = input("enter a city name:")
if (city in india):
    print(f"{city} is in india")
elif (city in pakistan):
    print(f"{city} in pakistan")
elif (city in bangladesh):
    print("city {city} in bangladesh")
else:
    print(f"i won't be able to tell you which country the {city} city is in!! sorry")
    
############### solution 2...... #####################

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter city 1: ")
city2 = input("Enter city 2: ")

if city1 in india and city2 in india:
    print("Both cities are in india")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("They don't belong to same country")


# Write a python program that can tell you if your sugar is normal or not.
#  Normal fasting level sugar range is 80 to 100.
# 1.....Ask user to enter his fasting sugar level
# 2...... If it is below 80 to 100 range then print that sugar is low
# 3......If it is above 100 then print that it is high otherwise print that it is normal
   ######################### solution 2 ##################
sugar=input("Please enter your fasting sugar level:")
sugar=float(sugar)
if sugar<80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar>100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")



