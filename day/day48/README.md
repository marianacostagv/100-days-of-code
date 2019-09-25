### Day 48
 
 - Intermediate Python for Data Science

**Link(s) usado(s) ou resultado(s):** 
 
 - [Intermediate Python for Data Science](https://campus.datacamp.com/courses/intermediate-python-for-data-science/dictionaries-pandas?ex=14 "Intermediate Python for Data Science")
 
 **New things learned:**
- While loop
- For loop:"for each var in seq, execute expression"
### enumerate
 `fam = [1.73, 1.68, 1.71, 1.89]`
`for index, height in enumerate(fam) :`
 `print("index " + str(index) + ": " + str(height))`
### Loop Data Structures: 
- Dictionary

`for key, value in world.items:`
`print(key + " -- " + str(value))`

- Numpy Arrays
` for val in np.nditer(my_array) :`

- DataFrame
##### iterrows
`for lab, row in brics.iterrows()
	print(lab)
	print(row)`
##### Selective print
 
` for lab, row in brics.iterrows() :
 print(lab + ": " + row["capital"])`
##### Add column

`for lab, row in brics.iterrows() :
brics.loc[lab, "name_length"] = len( row["country"])
print(brics)`

##### apply
`brics["name_length"] = brics["country"].apply(len)`
`cars["COUNTRY"] = cars["country"].apply(str.upper)`

---------------------

## [Files_used](https://github.com/mrncstt/100-days-of-code/tree/master/files/datacamp/python/Intermediate_Python_for_Data_Science "Files_used") :file_folder:
## [Log_day](https://github.com/mrncstt/100-days-of-code/blob/master/README.md "Log_day")  :scroll:
