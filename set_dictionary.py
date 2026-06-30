# Create a Python program that generates a set of unique numbers from a given list of numbers, then performs the following operations:
A=[1,2,3,'rohith','python']
# Adds new elements to the set
A.append('100r')
print(A)

# Removes existing elements from the set
B=set(A)
B.remove('rohith')
print(B)

# Performs union, intersection, and difference operations with another set
C={4,5,6,'rohith','python'}
print("Union:", B.union(C))
print("Intersection:", B.intersection(C))
print("Difference:", B.difference(C))

# Implement a dictionary-based data storage system that stores information about books in a library, including:
# Book title
# Author
# Publication year
# Genre
D={'The Great Gatsby': {'Author': 'F. Scott Fitzgerald', 'Publication Year': 1925, 'Genre': 'Novel'}}   
print(D)
# Write functions to:
# Add new books to the dictionary
# Remove existing books from the dictionary
# Search for books by title, author, or genre
# Display all books in the dictionary, sorted by title or author
add_book = lambda title, author, year, genre: D.update({title: {'Author': author, 'Publication Year': year, 'Genre': genre}})
remove_book = lambda title: D.pop(title, None) 
search_book = lambda key, value: {title: info for title, info in D.items() if info.get(key) == value}
display_books = lambda sort_by='title': sorted(D.items(), key=lambda x: x[1][sort_by.capitalize()]) if sort_by in ['title', 'author'] else D.items()    
# Test your implementation with sample data and verify that all operations work as expected.
# Adding new books
add_book('To Kill a Mockingbird', 'Harper Lee', 1960,       'Novel')
add_book('1984', 'George Orwell', 1949, 'Dystopian')
print(D)
