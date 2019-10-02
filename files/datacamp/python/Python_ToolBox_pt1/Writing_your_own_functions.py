'''
Writing your own functions
In this chapter, you'll learn how to write simple functions, as well as functions that
accept multiple arguments and return multiple values.
You'll also have the opportunity to apply these new skills to questions commonly encountered by data scientists.
'''
# Instructor: Hugo Bowne Anderson
# Write your own functions
# Defining your own functions
'''
value = int(input('insira um número:'))
#Docstrings: ""Return the square of value""
def square(value): #function header
    new_value = value**2 #<- function
    return new_value
num = square(value)
print(num)
    #print(new_value)
#square(value)

#When you define a function, you write parameters in the funcion header.
#When you call a function, you pass arguments into the function.
#Docstrings ""Return the square of value""
'''
'''
#Write a simple function
#Complete the function header by adding the appropriate function name, shout.
# In the function body, concatenate the string, 'congratulations' with another string, '!!!'. Assign the result to shout_word.
# Print the value of shout_word.
# Call the shout function.

# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations'+'!!!'
    # Print shout_word
    print(shout_word)

# Call shout
shout()

#Single-parameter functions
#Complete the function header by adding the parameter name, word.
# Assign the result of concatenating word with '!!!' to shout_word.
# Print the value of shout_word.
# Call the shout() function, passing to it the string, 'congratulations'.
# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')

#Functions that return single values
#In the function body, concatenate the string in word with '!!!' and assign to shout_word.
# Replace the print() statement with the appropriate return statement.
# Call the shout() function, passing to it the string, 'congratulations', and assigning the call to the variable, yell.
# To check if yell contains the value returned by shout(), print the value of yell.
# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    # Replace print with return
    return shout_word
# Pass 'congratulations' to shout: yell
yell = shout('congratulations')
print(yell)
'''
'''
#Multiple parameters and return values
number1 = int(input('insira o valor 1'))
number2 = int(input('insira o valor 2'))
def raise_to_power(number1, number2):
    new_value1 = number1**number2
    new_value2 = number2**number1
    new_tuple = (new_value1, new_value2)
    return new_tuple
result = raise_to_power(number1,number2)
print(result[1]) #The result will be a tuple too
'''
'''
#Functions with multiple parameters
#Modify the function header such that it accepts two parameters, word1 and word2, in that order.
# Concatenate each of word1 and word2 with '!!!' and assign to shout1 and shout2, respectively.
# Concatenate shout1 and shout2 together, in that order, and assign to new_shout.
# Pass the strings 'congratulations' and 'you', in that order, to a call to shout(). Assign the return value to yell.

# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1+'!!!'
    # Concatenate word2 with '!!!': shout2
    shout2 = word2+'!!!'
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1+shout2
    # Return new_shout
    return new_shout


# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations','you')

# Print yell
print(yell)

#A brief introduction to tuples
#Unpack nums to the variables num1, num2, and num3.
#Construct a new tuple, even_nums composed of the same elements in nums,
# but with the 1st element replaced with the value, 2.
nums = (3,4,6)
# Unpack nums into num1, num2, and num3
num1 = nums[0]
num2 = nums[1]
num3 = nums[2]

# Construct even_nums
even_nums = (2, num2, num3)
print(even_nums)

#Functions that return multiple values

#Modify the function header such that the function name is now shout_all, and it accepts two parameters, word1 and word2,
# in that order.
# Concatenate the string '!!!' to each of word1 and word2 and assign to shout1 and shout2, respectively.
# Construct a tuple shout_words, composed of shout1 and shout2.
# Call shout_all() with the strings 'congratulations' and 'you' and assign the result to yell1 and yell2
# (remember, shout_all() returns 2 variables!).

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1,shout2)
    # Return shout_words
    return shout_words


# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations','you')
# Print yell1 and yell2
print(yell1)
print(yell2)
#Hint
##Check that you have the correct number of parameters in the function header.
##You concatenate strings with the use of the + operator.
##Remember that tuples are constructed with parentheses ().
##Make sure you unpack the result of shout_all() into the correct number of variables. To unpack a 2-tuple tup into two variable a, b, execute a, b = tup
'''

# Bringing it all together
# Import the pandas package with the alias pd.
# Import the file 'tweets.csv' using the pandas function read_csv(). Assign the resulting DataFrame to df.
# Complete the for loop by iterating over col, the 'lang' column in the DataFrame df.
# Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count,
# add 1 to the value corresponding to this key in the dictionary, else add the key to langs_count and set the
# corresponding value to 1. Use the loop variable entry in your code.
'''
# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('C:\\Users\\Mariana\\PycharmProjects\\Python_DS_ToolxBox_pt1\\tweets.csv')
print(df)


# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count


# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)
'''
#Scope and user-defined functions