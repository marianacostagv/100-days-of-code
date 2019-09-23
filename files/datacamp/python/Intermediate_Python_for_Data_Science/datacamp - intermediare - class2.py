# DICTIONARIES
'''
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)
'''

'''
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin' #The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.

# Remove australia
del(europe['australia']) #Australia is not in Europe, Austria is! Remove the key 'australia' from europe.

# Print europe
print(europe)
'''
'''
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital']) #Use chained square brackets to select and print out the capital of France.

# Create sub-dictionary data
data = { 'capital':'rome', 'population':59.83 } #Create a dictionary, named data, with the keys 'capital' and 'population'. Set them to 'rome' and 59.83, respectively.

# Add data to europe under key 'italy'
europe['italy'] = data #Add a new key-value pair to europe; the key is 'italy' and the value is data, the dictionary you just built.

# Print europe
print(europe)
'''

# PANDAS
'''
import pandas as pd
brics = pd.read_csv('C:/Users/Mariana/PycharmProjects/datacamp/brics.csv', index_col=0)
print(brics)
'''
# Dictionary to DataFrame (1)
'''
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country':['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right':[True, False, False, False, True, True, True],
    'cars_per_cap':[809, 731, 588, 18, 200, 70, 45]

}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
'''
'''
#Index and Select Data
#Column Access[]
##Square Brackets (1)
# Import cars data
import pandas as pd
#cars = pd.read_csv('cars.csv', index_col = 0)
cars = pd.read_csv('C:/Users/Mariana/PycharmProjects/datacamp/cars_datacamp.csv', index_col=0)
#print(cars)
# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country","drives_right"]])
## Square Brackets (2)
# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
##loc and iloc (1)
# Print out observation for Japan
print(cars.loc["JPN"])

# Print out observations for Australia and Egypt
print(cars.loc[["AUS","EG"]])

##loc and iloc (2)
# Print out drives_right value of Morocco
print(cars.loc[["MOR"],["drives_right"]])

# Print sub-DataFrame
print(cars.iloc[[4,5], [1,2]]) #Printed the5º en 6º elements from de 2ª and 3º criterias

##loc and iloc (3)
# Print out drives_right column as Series
print(cars["drives_right"])

# Print out drives_right column as DataFrame
print(cars[["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars[["cars_per_cap","drives_right"]])
'''
'''
##Comparison Operators
##In the editor on the right, write code to see if True equals False.
# Write Python code to check if -5 * 15 is not equal to 75.
# Ask Python whether the strings "pyscript" and "PyScript" are equal. What happens if you compare booleans and integers?
# Write code to see if True and 1 are equal.

# Comparison of booleans
True == False

# Comparison of integers
-5 * 15 != 75

# Comparison of strings
"pyscript" == "PyScript"

# Compare a boolean with an integer
True == 1
# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print("test" <= y)

#Comparison of booleans
print(True > False)
#
# Create arrays
import numpy as np

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < 3 * your_kitchen)
'''
'''
# Boolean operators with Numpy
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11,your_house<11))
'''
'''
#Conditional statement: if, elif, else
# Define variables
## Examine the if statement that prints out "Looking around in the kitchen." if room equals "kit".
# Write another if statement that prints out "big place!" if area is greater than 15.
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print("big place")
else:
    print("bla")

# Customize further: elif
##Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")
'''
# Filtering Pandas DataFrame
# Driving right (1)
# Extract the drives_right column as a Pandas Series and store it as dr.
# Use dr, a boolean Series, to subset the cars DataFrame.
# Store the resulting selection in sel. Print sel, and assert that drives_right is True for all observations.
# Import cars data
import pandas as pd

cars = pd.read_csv('C:/Users/Mariana/PycharmProjects/datacamp/cars_datacamp.csv', index_col=0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)
# Driving right (2)
# Convert the code on the right to a one-liner that calculates the variable sel as before.
# Import cars data
import pandas as pd

cars = pd.read_csv('C:/Users/Mariana/PycharmProjects/datacamp/cars_datacamp.csv', index_col=0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Cars per capita (1)
# Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
# Use cpc in combination with a comparison operator and 500.
# You want to end up with a boolean Series that's True if the corresponding
# country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
# Use many_cars to subset cars, similar to what you did before.
# Store the result as car_maniac.
# Print out car_maniac to see if you got it right.
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('C:/Users/Mariana/PycharmProjects/datacamp/cars_datacamp.csv', index_col=0)
# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

'''
# Cars per capita (2)
# Use the code sample above to create a DataFrame medium,
# that includes all the observations of cars that have a cars_per_cap between 100 and 500.

# Print out medium
# Import cars data
import pandas as pd

cars = pd.read_csv('C:/Users/Mariana/PycharmProjects/datacamp/cars_datacamp.csv', index_col=0)

# Import numpy, you'll need this
# noinspection PyUnresolvedReferences
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
#medium = np.logical_and(cars['cars_per_cap'] < 500, cars['cars_per_cap'] > 100)
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
# Print medium
print(medium)