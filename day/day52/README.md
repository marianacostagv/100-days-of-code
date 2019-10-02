### Day 52
 - Importing Data in Python (Part 1)
 - Python Data Science Toolbox (Part 1)

**Link(s) usado(s) ou resultado(s):** 
 
 - [Importing Data in Python (Part 1)](https://www.datacamp.com/courses/importing-data-in-python-part-1 "Importing Data in Python (Part 1)")
 - [Python Data Science Toolbox (Part 1)](https://www.datacamp.com/courses/python-data-science-toolbox-part-1 "Python Data Science Toolbox (Part 1)")
 
 **New things learned:**
- Reading a text file
- Reading a CSV file: Numpy and Pandas
### Numpy
- NumPy arrays: standard for storing numerical data
- Essential for other packages: e.g. scikit-learn

`import numpy as np`\
`filename = 'MNIST.txt`\
`data = np.loadtxt(filename, delimiter=',',skiprows=1, usecols=[0, 2])`\
`print(data)`

### Pandas: 
-Exploratory data analysis:
- Data wrangling
- Data preprocessing
- Building models
- Visualization

` import pandas as pd`\
` filename = 'winequality-red.csv'`\
` data = pd.read_csv(filename)`\
` data.head()`

#Convert Pandas into Numpy
- `data_array = data.values`

---------------------

## [Files_used](https://github.com/mrncstt/100-days-of-code/tree/master/files/datacamp/python/Intermediate_Python_for_Data_Science "Files_used") :file_folder:
## [Log_day](https://github.com/mrncstt/100-days-of-code/blob/master/README.md "Log_day")  :scroll:
