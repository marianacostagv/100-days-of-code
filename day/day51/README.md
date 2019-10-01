'''
Writing your own functions
In this chapter, you'll learn how to write simple functions, as well as functions that
accept multiple arguments and return multiple values.
You'll also have the opportunity to apply these new skills to questions commonly encountered by data scientists.
'''
#Instructor: Hugo Bowne Anderson
#Write your own functions
#Defining your own functions
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

