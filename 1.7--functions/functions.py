# 1.....Write a function called calculate_area that 
# takes base and height as an input and returns
#  and area of a triangle. Equation of an area 
# of a triangle is,  area = (1/2)*base*height////
# def areaTriangle(b, h):
#     return 0.5 * b * h

# base = 8
# height = 9
# print('Area = {:.2f}' .format(areaTriangle(base, height)))





# 2.... Modify above function to take third parameter
#  shape type. It can be either "triangle" or "rectangle".
#  Based on shape type it will calculate area. Equation 
# of rectangle's area is, rectangle area = length*width////
# If no shape is supplied then it should take triangle as a default shape
def calculate_area(dimension1,dimension2,shape="triangle"):
    '''
    :param dimension1: In case of triangle it is "base". For rectangle it is "length".
    :param dimension2: In case of triangle it is "height". For rectangle it is "width".
    :param shape: Either "triangle" or "rectangle"
    :return: Area of a shape
    '''
    if shape=="triangle":
        area=1/2*(dimension1*dimension2) # Triangle area is : 1/2(Base*Height)
    elif shape=="rectangle":
        area=dimension1*dimension2 # Rectangle area is: Length*Width
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area




# Write a function called print_pattern that takes integer number
#  as an argument and prints following pattern if input number is 3,
# if input 4 then it should print 
# Basically number of lines it prints is equal to that number.
#  (Hint: you need to use two for loops)
def print_pattern(n=5):
    for i in range(n):
        s = ""
        for j in range(i+1):
            s = s+ '*'
        print(s)
