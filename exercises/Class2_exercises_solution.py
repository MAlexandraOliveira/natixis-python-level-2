'''
EXERCISES FOR CLASS 2
'''


'''
Exercise 1

Write a lambda function that takes in two arguments and returns their sum.

'''
# ANSWER
sum_lambda = lambda x, y: x + y
print(sum_lambda(3, 5))  # Output: 8


'''
Exercise 2

Write a lambda function that takes in one argument and returns its square.

'''
# ANSWER
square_lambda = lambda x: x ** 2
print(square_lambda(4))  # Output: 16


'''
Exercise 3

Write a lambda function that takes in two arguments and returns the maximum of the
two.

'''
# ANSWER
max_lambda = lambda x, y: max(x, y)
print(max_lambda(10, 7))  # Output: 10


'''
Exercise 4

Write a lambda function that computes the square root of a given number and 
returns the rounded result with two decimal places.

'''
# ANSWER
import math
sqrt_lambda = lambda x: round(math.sqrt(x), 2)
print(sqrt_lambda(25))  # Output: 5.0


'''
Exercise 5

Write a lambda function that retrieves the highest absolute value of a 
given list with negative and positive values.

'''
# ANSWER
max_abs_lambda = lambda lst: max(lst, key=abs)
print(max_abs_lambda([-5, 3, -7, 9, -2]))  # Output: -7


'''
Exercise 6

Write a lambda function that takes in one argument and returns True if the number is
positive and False if the number is negative.

'''
# ANSWER
check_positive_lambda = lambda x: True if x > 0 else False
print(check_positive_lambda(-3))  # Output: False


'''
Exercise 7

Write a lambda function that takes in one argument (a string) and returns the string in reverse order.

'''
# ANSWER
reverse_string_lambda = lambda s: s[::-1]
print(reverse_string_lambda("hello"))  # Output: "olleh"


'''
Exercise 8

Write a lambda function that takes in two arguments (a string and a prefix) and 
returns the string with the prefix added.

'''
# ANSWER
add_prefix_lambda = lambda s, prefix: prefix + s
print(add_prefix_lambda("world", "hello "))  # Output: "hello world"


'''
Exercise 9

Write a lambda function that takes in a list of words and a length and returns a new
list with only the words that have the given length.

'''
# ANSWER
filter_by_length_lambda = lambda words, length: [word for word in words if len(word) == length]
print(filter_by_length_lambda(['apple', 'banana', 'kiwi', 'orange'], 5))  # Output: ['apple', 'banana']


'''
Exercise 10

Write a lambda function that takes in a list of numbers and returns a new list with
only the even numbers.

'''
# ANSWER
filter_even_lambda = lambda numbers: [num for num in numbers if num % 2 == 0]
print(filter_even_lambda([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]


'''
Exercise 11

Write a lambda function that takes in a list of words and returns a new list with the
length of each word.

'''
# ANSWER
word_lengths_lambda = lambda words: [len(word) for word in words]
print(word_lengths_lambda(['apple', 'banana', 'kiwi']))  # Output: [5, 6, 4]


'''
Exercise 12

Create a list of tuples where each tuple contains corresponding elements from two
different lists using zip function in list comprehension.

'''
# ANSWER
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
tuple_list = [(x, y) for x, y in zip(list1, list2)]
print(tuple_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


'''
Exercise 13

Create a generator expression for all even numbers from 0 to 10.

'''
# ANSWER
even_numbers_gen = (num for num in range(11) if num % 2 == 0)
print(list(even_numbers_gen))  # Output: [0, 2, 4, 6, 8, 10]


'''
Exercise 14

Write a lambda function that takes in a list of numbers and returns True if all the
elements in the list are positive and False otherwise.

'''
# ANSWER
all_positive_lambda = lambda numbers: all(num > 0 for num in numbers)
print(all_positive_lambda([1, 2, 3, 4]))  # Output: True
print(all_positive_lambda([-1, 2, 3, 4]))  # Output: False


'''
Exercise 15

Write a lambda function that takes in a list of numbers and returns True if any of the
elements in the list are positive and False otherwise.

'''
# ANSWER
any_positive_lambda = lambda numbers: any(num > 0 for num in numbers)
print(any_positive_lambda([-1, -2, -3, 4]))  # Output: True
print(any_positive_lambda([-1, -2, -3]))  # Output: False


'''
Exercise 16

Write a Python function that takes in a list and returns a sorted list in descending order. 

'''
# ANSWER
descending_sort_lambda = lambda lst: sorted(lst, reverse=True)
print(descending_sort_lambda([5, 2, 7, 1, 9]))  # Output: [9, 7, 5, 2, 1]


'''
Exercise 17

Write a lambda function that takes in a list of dictionaries and returns a new list
sorted by the value of a given key.

'''
# ANSWER
sort_by_key_lambda = lambda list_of_dicts, key: sorted(list_of_dicts, key=lambda x: x[key])
print(sort_by_key_lambda([{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 20}], 'age'))
# Output: [{'name': 'Alice', 'age': 20}, {'name': 'John', 'age': 25}]


'''
Exercise 18

Write a lambda function that takes in a string and returns True if the string is a palindrome and False otherwise.

'''
# ANSWER
is_palindrome_lambda = lambda s: s == s[::-1]
print(is_palindrome_lambda("radar"))  # Output: True
print(is_palindrome_lambda("hello"))  # Output: False


'''
Exercise 19

Write a lambda function that takes in a list of strings and returns a new list with only the strings that start with a 
vowel (a, e, i, o, u).

'''
# ANSWER
starts_with_vowel_lambda = lambda strings: [s for s in strings if s[0].lower() in ['a', 'e', 'i', 'o', 'u']]
print(starts_with_vowel_lambda(['apple', 'banana', 'kiwi', 'orange']))  # Output: ['apple', 'orange']


'''
Exercise 20

Write a lambda function that takes in a list of tuples, where each tuple contains a name and an age, and 
returns the names of people who are above 18 years old.

'''
# ANSWER
above_18_lambda = lambda people: [name for name, age in people if age > 18]
print(above_18_lambda([('John', 25), ('Alice', 16), ('Bob', 30)]))  # Output: ['John', 'Bob']
