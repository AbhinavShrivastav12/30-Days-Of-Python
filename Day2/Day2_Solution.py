from math import pi
# Exercise all soultion are solved here!!!
# 1. Declare a first name variable and assign a value to it
first_name = 'Abhinav'
# 2. Declare a last name variable and assign a value to it
last_name = 'Shrivastav'
# 3. Declare a full name variable and assign a value to it
full_name = 'Abhinav Shrivastav'
# 4. Declare a country variable and assign a value to it
country = 'Nepal'
# 5. Declare a city variable and assign a value to it
city = 'Lumbini'
# 6. Declare an age variable and assign a value to it
age = 23
# 7. Declare a year variable and assign a value to it
year = 2002
# 8. Declare a variable is_married and assign a value to it
is_married = 'unmarried'
# 9. Declare a variable is_true and assign a value to it
is_true = True
# 10. Declare a variable is_light_on and assign a value to it
is_light_on = True
# 11. Declare multiple variable on one line
first_name, last_name, is_light_on = 'Abhinav' , 'Shrivastav', True
# Showing the output
print(first_name) 
print(last_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
print(first_name,last_name,is_light_on)

# Level 2
# 12. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))

# 13. Using the len() built-in function, find the length of your first name
print(len(first_name))
# 14. Compare the length of your first name and your last name
len_firstName = len(first_name)
len_lastName = len(last_name)
if (len_firstName > len_lastName) :
    print("First name is greater then the  last name")
else: 
    print("Last name is greater than first name")

# 15. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# 16. Add num_one and num_two and assign the value to a variable total
total = sum([num_one,num_two])
print('Total',total)
# 17. Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
print("Difference", diff)

# 18. Multiply num_two and num_one and assign the value to a variable product
product = num_one*num_two
print('Multiply', product)

# 19. Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
print("Division", division)

# 20. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print("Remainder" ,remainder)

# 21. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print("Exp", exp)

# 22. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("Floor Division", floor_division)

# 23. The radius of a circle is 30 meters. 
  #  i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area_of_circle = pi * radius ** 2 
print("Area of circle:" , area_of_circle)
  # ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*pi*radius
print("Circumfrence of he circle", circum_of_circle)

# iii. Take radius as user input and calculate the area.
user_radius = float(input("Enter the radius of the circle?"))
user_area = pi * user_radius ** 2
print("the area of the circle is: ", user_area)