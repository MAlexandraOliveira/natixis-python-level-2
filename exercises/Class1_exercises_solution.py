'''
Exercise 1

Write a Python function that prints "Hello, World!" to the console. The function simply prints a string to the console.
The purpose of this exercise is to help you understand how to write a function in Python.

'''

# ANSWER
def print_hello_world():
    print("Hello, World!")

# Test the function
print_hello_world() # Output: "Hello, World!"


'''
Exercise 2

Write a Python function that calculates the sum of the digits of a positive integer. 
The function takes a positive integer as input and returns the sum of its digits.

'''

# ANSWER
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Test the function
print(sum_of_digits(123))  # Output: 6


'''
Exercise 3

Write a Python function that reverses a given string. 
The function takes a string as input and returns its reverse.

'''

# ANSWER
def reverse_string(s):
    return s[::-1]

# Test the function
print(reverse_string("hello"))  # Output: "olleh"


'''
Exercise 4

Write a Python function that checks if a given string is a palindrome. The
function takes a string as input and returns True if it is a palindrome, False otherwise.

'''

# ANSWER
def is_palindrome(s):
    return s == s[::-1]

# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False


'''
Exercise 5

Write a Python function that checks if a given number is a prime number. The
function takes a number as input and returns True if it is a prime number, False otherwise.

'''

# ANSWER
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(17))  # Output: True
print(is_prime(15))  # Output: False


'''
Exercise 6

Write a Python function that generates the Fibonacci series up to a given number.
The function takes a number as input and generates the Fibonacci series up to that number.

'''

# ANSWER
def fibonacci(n):
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Test the function
print(fibonacci(100))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


'''
Exercise 7

Write a Python function that calculates the factorial of a given number. 
The function takes a number as input and returns its factorial.

'''

# ANSWER
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120


'''
Exercise 8

Write a Python function that removes duplicates from a given list. 
The function takes a list as input and returns a new list without duplicates.

'''

# ANSWER
def remove_duplicates(lst):
    return list(set(lst))

# Test the function
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]


'''
Exercise 9

Create a list of all even numbers from 0 to 10 using list comprehension.

'''

# ANSWER
even_numbers = [num for num in range(11) if num % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10]


'''
Exercise 10

Create a dictionary where keys are numbers from 1 to 10 and values are their
squares using dictionary comprehension.

'''

# ANSWER
squares_dict = {num: num**2 for num in range(1, 11)}
print(squares_dict)


'''
Exercise 11

Create a set of all even numbers from 0 to 10 using set comprehension.

'''

# ANSWER
even_numbers_set = {num for num in range(11) if num % 2 == 0}
print(even_numbers_set)


'''
Exercise 12

Write a Python function that uses list comprehension to create a new list from a given list. 
The function takes a list as input and returns a new list with certain elements.

'''

# ANSWER
def filter_list(lst):
    return [x for x in lst if x > 0]

# Test the function
print(filter_list([-1, 2, 3, -4, 5]))  # Output: [2, 3, 5]


'''
Exercise 13

Write a Python function that creates a list of all numbers from a start number (e.g. 0) to an 
end number (e.g. 10) which are divisible by 2 and 5 using list comprehension.

'''

# ANSWER
def divisible_by_2_and_5(start, end):
    return [num for num in range(start, end + 1) if num % 2 == 0 and num % 5 == 0]

# Test the function
print(divisible_by_2_and_5(0, 10))  # Output: [0, 2, 4, 6, 8, 10]


'''
Exercise 14

Write a Python function that merges two given lists into a new list. 
The function takes two lists as input and returns a new list with the elements of both lists.

'''

# ANSWER
def merge_lists(list1, list2):
    return list1 + list2

# Test the function
print(merge_lists([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]


'''
Exercise 15

Write a Python function that creates a creates a NxM matrix using nested list comprehension.
The Python parameters default for N and M should be, respectively, 3 and 4.

'''

# ANSWER
def create_matrix(n=3, m=4):
    return [[0 for _ in range(m)] for _ in range(n)]

# Test the function
print(create_matrix())  # Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


'''
Exercise 16

Write a Python function that creates a flattened list from a list of lists using nested list comprehension.

'''

# ANSWER
def flatten_list(list_of_lists):
    return [element for sublist in list_of_lists for element in sublist]

# Test the function
print(flatten_list([[1, 2, 3], [4, 5], [6, 7, 8]]))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


'''
Exercise 17

Write a Python function that reverses a given list. 
The function takes a list as input and returns its reverse.

'''

# ANSWER
def reverse_list(lst):
    return lst[::-1]

# Test the function
print(reverse_list([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]


'''
Exercise 18

Write a Python function that creates a pandas DataFrame from two given lists.
The function takes two lists as input and returns a pandas DataFrame with the elements of both lists.

'''

# Assuming pandas is imported already
import pandas as pd

# ANSWER
def create_dataframe(list1, list2):
    return pd.DataFrame({'Column1': list1, 'Column2': list2})

# Test the function
print(create_dataframe([1, 2, 3], ['a', 'b', 'c']))


'''
Exercise 19

Write a Python function that removes vowels from a given string. 
The function takes a string as input and returns a string without vowels.

'''

# ANSWER
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)

# Test the function
print(remove_vowels("Hello, World!"))  # Output: "Hll, Wrld!"


'''
Exercise 20

Write a Python function that capitalizes the first letter of each word in a given sentence. 
The function takes a string as input and returns a new string with the first letter of each word capitalized.

'''

# ANSWER
def capitalize_first_letter(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

# Test the function
print(capitalize_first_letter("hello world"))  # Output: "Hello World"
