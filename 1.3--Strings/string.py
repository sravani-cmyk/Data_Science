# Create 3 variables to store street, city and country, now create 
# address variable to store entire address. Use two ways of creating 
# this variable, one using + operator and the other using f-string. Now
#  Print the address in such a way that the street, city and country prints in a separate line //
######################### solution ##################
street = "naali_pattu"
city = "hyderabad"
country = "India"
Address = street + '\n' +city+ '\n' +country
print("Address using + operator: ",Address)
Addr_f_str = f'{street}\n{city}\n{country}'
print("Address using f_string:", Addr_f_str)



# Create a variable to store the string "Earth revolves around the sun"
   # Print "revolves" using slice operator
   # Print "sun" using negative index  //
##################### solution #######################
var_1 ="Earth revolves around the sun"
print(var_1[6:15])
print(var_1[-3:])


# Create two variables to store how many fruits and vegetables you eat
#  in a day. Now Print "I eat x veggies and y fruits daily" where x and y
#  presents vegetables and fruits that you eat everyday. Use python f string for this.//
##################### solution ############################
fruits = 10
vegies = 7
print(f"total fruits are {fruits} and vegies are {vegies} in a day ")


# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong 
# statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words 
# in original strong with new ones and print the new string. Also try to do this in one line.//
#################### solution ################################
s='maine 200 banana khaye'
s1 = s.replace('banana','samosa').replace('200','10')
print("single line replacement:",s1)
