#1..... After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
print ("\n Exercise 1\n")
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == "heads":
        count += 1
print("Heads count:",count)

 # 1.... Print square of all numbers between 1 to 10 except even numbers
print("\nExercise2\n")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)
# 2....Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]//

# Write a program that asks you to enter an expense amount and program should
#  tell you in which month that expense occurred. If expense is not found then 
# it should print that as well.//
print("\n Exercise\n")
month_list = ["january","February","March","April","May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input["Enter expenses amount:"]
e = int(e)
month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i 
        break
if month != -1:
    print(f"you spent {e} in {month_list[month]}")
else:
    print(f"you didn't spend {e} in any month")
# Lets say you are running a 5 km race. Write a program that,

    # 1.... Upon completing each 1 km asks you "are you tired?"
    # 2....If you reply "yes" then it should break and print "you didn't finish the race"
    # 3.....If you reply "no" then it should continue and ask "are you tired" on every km
    # 4.....If you finish all 5 km then it should print congratulations message //

print("\nExercise 4 \n")
for i in range(5):
    print(f"you ran {i+1} miles")
    tierd = input("Are you tierd ")
    if tierd == "yes":
        break

if i == 4:
    print("Hurry up you are a rock star you just finished 4 kms range")
else:
    print("you didn't finish 5 km but hey congrats anyways! you will run {i+1} miles")


# 5.....Write a program that prints following shape
# *
# **
# ***
# ****
# *****
#////////
for i in range(1,6):
    s = ""
    for i in range(i):
        s += '*'
    print(s)
    


