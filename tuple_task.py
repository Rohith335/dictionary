# Create a Python script that generates a tuple containing the names of 5 different cities.
cities=('warangal', 'hyderabad', 'Hanamkonda', 'kazipet', 'karimnagar')
# Write a function that takes a tuple as an argument and returns the first and last elements of the tuple.
def get_first_and_last(t):
    return t[0], t[-1]
# Create a tuple of tuples, where each inner tuple contains a student's name and their corresponding grade (e.g., ( ("John", 85), ("Alice", 92) )).
students = (("John", 85), ("Alice", 92), ("Bob", 78), ("Charlie", 95), ("Diana", 88))           
# Implement a function that takes the tuple of tuples from the previous task and returns a new tuple with the students' names sorted in alphabetical order.
def get_sorted_student_names(student_tuple):
    return tuple(sorted([name for name, grade in student_tuple]))
# Practice tuple unpacking by writing a function that takes a tuple of 3 elements and assigns each element to a separate variable, then prints out the values of these variables.
def unpack_tuple(t):
    a, b, c = t
    print(a, b, c)