### Day 47

 - Intermediate Python for Data Science

**Link(s) usado(s) ou resultado(s):** 

 - [Intermediate Python for Data Science](https://campus.datacamp.com/courses/intermediate-python-for-data-science/dictionaries-pandas?ex=14 "Intermediate Python for Data Science")

 **Nova(s) coisa(s) aprendida(s):**
- Comparison Operators: how Python values relate
- Boolean | And | Or | Not
### Numpy: 
##### np.logical_and(bmi>21, bmi<22)
##### np.logical_or
##### np.logical_not
### Conditional statments: if, elif, else
#### Filtering Pandas DataFrame
##### Goal: select contries with are over 8 mm km² 
###### Step 1: select the area comumn :arrow_right: brics["area"] or brics.loc[:"area"] or brics.iloc[:,2]
###### Step 2: do comparison on area column :arrow_right: is_huge = brics["area"] >8
###### Step 3: use result to select countries :arrow_right: brics[is_huge]
