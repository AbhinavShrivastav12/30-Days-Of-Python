# 1. Declare your age as integer variable
age = 23
# 2. Declare your height as a float variable
height = 5.70
# 3. Declare a variable that store a complex number
complex_num = (3+4j)
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
base = int(input("Enter the base of the triangle :"))
height_Triangle = int(input("Enter the height of the triangle :"))
area = base*height_Triangle*0.5
print("The area of the triangle is :",area)
#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    # Enter side a: 5
    # Enter side b: 4
    # Enter side c: 3
    # The perimeter of the triangle is 12
side_a = int(input("\nEnter the side a of the triangle: "))
side_b = int(input("Enter the side b of the triangle: "))
side_c = int(input("Enter the side c of the triangle: "))
perimeter = side_a+side_b+side_c
print("The perimeter of the triangle is :", perimeter)
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("\nEnter the length of a rectangle :"))
width = int(input("Enter the width of a rectangle :"))
area_Rect = length*width
perimeter_Rect = 2*length*width
print("The area of the rectangle is :" ,area_Rect)
print("The perimeter of the rectangle is :",perimeter_Rect)
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("\nEnter the radius of teh circle: "))
pi = 3.14
area_circle = pi*radius**2
circumference = 2*pi*radius
print("The area of the circle is : ",area_circle)
print("The circumference of the circle is: ",circumference)
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2 #slope
y_intercept = 2*0-2 #when x=0
x_intercept = (0+2) / 2 #when y=0
print("\nSlope: ",m)
print("Y intercept : 0,",y_intercept)
print("X intercept :", x_intercept, ",0")
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,y1 = 2,2
x2,y2 = 6,10
slope = (y2-y1)/(x2-x1)
distance = ((x2-x1)**2+(y2-y1)**2)**0.5
print("\nSlope is :",slope)
print("Euclidean distance: ",distance)
# 10. Compare the slopes in tasks 8 and 9.
compare = m>=slope and m<=slope
print("\nComparison: ",compare)
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range (-10,10):
    y = x**2 + 6*2 +9
    print("\nX=", x ,"Y=",y)
x = -3
y = x**2 + 6*x +9
print("\nAt X = ",x ,"and Y =" ,y)
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len('python')
length_dragon = len('dragon')
comparison = length_python>length_dragon
print("Length of the python :",length_python)
print("Length of the dragon :",length_dragon)
print("Flasy comparison :", comparison)
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
result = ('on' in 'python') and ('on' in 'dragon')
print("To find letter 'on' is found in  'python' and 'dragon' :",result)
# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
text = 'I hope this course is not full of jargon'
check = 'jargon' in text
print("Result :",check)
# 15. There is no 'on' in both dragon and python
answer = not(('on' in 'python') and ('on' in 'dragon'))
print("There is no 'on' in python and in dragon :",answer)
# 16. Find the length of the text python and convert the value to float and convert it to string
change = float(length_python)
change_again = str(change)
print("Float value :",change)
print("Into string :",change_again)
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
n = int(input("Enter the number :"))
result_check = (n%2==0)
if (result_check):
    print("Even numbers are divisible by 2 and the remainder is zero : ",n)
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
number = 7//3
converted_value = 2.7
check_result = number == converted_value
print("Is the floor divisiona and converted value is equal :",check_result)
# 19. Check if type of '10' is equal to type of 10
integer = type(10)
print("\nType of 10 :")
string = type('10')
print("Type of '10'")
equal = (integer == string)
print("Checking type of 10 is equal to type of '10' :",equal)
# 20. Check if int('9.8') is equal to 10
given_number = int(9.8)
checking_number = 10
equallism = (given_number == checking_number)
print("Checking int('9.8') is equal to 10 :",equallism)
# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#      Enter hours: 40
#      Enter rate per hour: 28
#      Your weekly earning is 1120
hours = int(input("\nEnter the hour :"))
rate_per_hour = int(input("Enter the rate per hour :"))
weekly_earning = hours*rate_per_hour
print("Your weekly earning :",weekly_earning)
# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#     Enter number of years you have lived: 100
#     You have lived for 3153600000 seconds.
number_of_years = int(input("\nEnter the number of years ypu have lived: "))
years = 365*24*60**2
number_of_seconds = number_of_years*years
print(" You have lived for",number_of_seconds,"seconds.")
# 23. Write a Python script that displays the following table
#      1 1 1 1 1
#      2 1 2 4 8
#      3 1 3 9 27
#      4 1 4 16 64
#      5 1 5 25 125
 
# 24. Write a Python script that displays the following table
#      1 1 1 1  1 1
#      2 1 2 4  1 8
#      3 1 3 9  1 27
#      4 1 4 16 1 64
#      5 1 5 25 1 125
#      6 1 6 36 1 216
for j in range(1,7) :
    print(j,1,j,j**2,1,j**3)