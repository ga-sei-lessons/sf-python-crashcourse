# this is a comment -- will not be executed 

# multi
# line
# comment

"""
this is a doc string -- we will learn more about this kind of special comment later
more than one line
"""

# variables use 'snake_case' -- lowercase and spaces get underscores
my_var = 'hello snakes!'

# print(my_var)

# ## # ## # ## # ##
# DATA TYPES 

# Bools
None # falsey -- like null and undefined all in one
True # a truthy bool
False # Falsey bool

# Text type
str # string constuctor 
# literals
my_string = "double qoutes a cool"
my_other_string = 'single qoutes are fine too'

# Number types
# integers -- whole numbers
int
my_int = 30
# floating points or floats -- decimals
float
my_float = 1.0978234
# complex nums
complex 
my_complex = 3j 
my_other_complex = 2j

# Container types
# List (aka an array)
list
my_li = [0, 1, 5, 'hello', 'big snakes']
# Dictionary (aka object -- but not in python)
dict # these are distinct from objects in python
my_dictionary = {
  'animal': 'snakes'
}

# ## # ## # ##
# Control flow w if/else

# three bools
None
True
False

# logical operators
# and # && 
# or  # ||
# not or ! # !

# comparison operators
# == # equality
# > # who is bigger wakkas
# <
# >=
# <=

# my_bank_account = True
# amount_of_money = 500

# # conditionals start with if keyword
# if my_bank_account and amount_of_money >= 1000:
#   print('you are ballin')
# elif my_bank_account: # elif = else if
#   print('put more money in the bank!')
# else:
#   print('you should get some money!')

# ## # ## # ## # 
# Functions and Variable scope

# def keyword makes a function
def greet(name):
  # indentation block
  # hello i am in the scope of the function
  # print('Hello, ' + name) # string concatenation
  # format string
  s = 'spam'
  # print(f'Hello, {name} {s} {s} {s} {s}')
  # format template
  print('Hello, {} {} {}'.format(name, s, name))

# invokation of the funciton
# greet('April')

# # scope in python
# e = 'eggs'

# def exclaim():
#   global e = 'spam'
#   print(f'but I dont like spam with my {e}')

# exclaim()

# example of using a doc string
def my_well_documented_function():
  '''
    this is a well documented funciton, it uses a doc string, prints hello\n
    my_well_documented_function(None):\n
      returns None
  '''
  print('hello')

my_well_documented_function()

# ## # ## # ## # ## #
# Math

# math operators
# +, -, =, /, *, %
## ** to the power of
## // forced integer division
# print(10 + 10)
# print(2 ** 7) # 2 ^ 7
# print(15 // 2.7) # forced integer division floors the output

# my_complex = 1 + 3j + 5j + 2
# print(my_complex)

# print(1 + int("1")) # python will not do automatic conversion ot types

# ## # ## # ## #
# String instance methods

my_str = 'spam and eggs'

# print the satring directory to see all of the methods
# print(dir(str))

# spam_list = my_str.split(" ") # split on the whitespace
# print(spam_list)

# print(my_str.upper())
# print(my_str.lower())

# # finding the length of a string
# print(len(my_str))

# # in keyword to find if a string contains a substring
# print("sausage" in my_str)

# ## # ## # ## #
# Lists and list methods

my_list = ['spam', 'eggs', 'bacon', 'sausage']

# check the length of a list
print(len(my_list))

# making a list with mult
# print(['spam'] * 10000)

# access values with numbers counting from 0 -- out of bounds is an error
# print(my_list[3])

print(dir(list))
# this is push
my_list.append('spam')
# this is unshift
# list.insert(index, item)
my_list.insert(0, 'spam')
# remove the last spam
my_list.pop()
# remove finds a value and takes it ouw
if 'eggs' in my_list: 
  my_list.remove('eggs')
if 'eggs' in my_list: 
  my_list.remove('eggs')
# print(my_list.reverse())

# ## # ## # ## # ## 
# string and list slicing

# this works on strings and lists
my_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list/str[start index:end index:steps]

# make copy of of the list
print(my_nums[::])

# remove first thing in the list
print(my_nums[1::])

print(my_nums[1:3]) # omit colon for default step by 1

# every other item in the list
print(my_nums[::2]) # start @ default, end @ default, count by 2

# slice off the last
print(my_nums[len(my_nums) - 1::])

# reverse with a step of -1
print(my_nums[::-1])

# wrap the end -- all but the last
print(my_nums[:-1:])

my_str = '0123456789'
print(my_str[:-1])