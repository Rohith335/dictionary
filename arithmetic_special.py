# Implement a Python program that uses arithmetic operators (+, -, *, /, %, **) to calculate the area and perimeter of a rectangle, given its length and width as input.
length=int(input("enter length: "))
width=int(input("enter width: ")) 
area_of_rectangle= length * width
perimeter_of_rectangle= 2 * (length + width)
print("area of rectangle: ", area_of_rectangle)
print("perimeter of rectangle: ", perimeter_of_rectangle )

# Create a Python function that takes two numbers as input and uses comparison operators (>, <, ==, !=, >=, <=) to determine which number is larger, smaller, or if they are equal, then print out the results.
A=int(input("enter a number: "))
B=int(input("enter a number: "))
if A>B:
    print("A is larger")
elif A<B:
    print("B is larger")
elif A==B:
    print("Both are equal")
elif A!=B:
    print("both are not equal")
elif A>=B:
    print("A is greater than B")
elif A<=B:
    print("B is greater than A")
# Write a Python script that uses logical operators (and, or, not) to evaluate basic conditional statements, such as determining if a number is within a certain range or if a string matches a specific pattern.
val=int(input("enter a number: "))
if val>10 and val<20:
    print("The number is between 10 and 20")    
elif val<10 or val>20:
    print("The number is not between 10 and 20")    
elif not(val>10 and val<20):
    print("The number is not between 10 and 20")

# Use the assignment operator (=) and the augmented assignment operators (+=, -=, *=, /=, %=, **=) to update variable values in a Python program, demonstrating their differences and use cases.
x=int(input)("enter a number: ")
print("Initial value of x:", x)
x+=5
print("After x += 5:", x)
x-=3
print("After x -= 3:", x)
x*=2
print("After x *=2:", x)
x/=2
print("After x /=2:", x)
x%=2
print("After x %=2:", x)
x**=3
print("After x **=3:", x)

# Develop a Python program that utilizes the identity operators (is, is not) and membership operators (in, not in) to check if two variables refer to the same object or if an element is present in a list or string.
R=int(input("enter a number: "))
S=int(input("enter a number: "))
print(R is S)
print(R is not S)
T='python'
res= 'p' in T
print(res)
U= 'n' not in T
print(res)