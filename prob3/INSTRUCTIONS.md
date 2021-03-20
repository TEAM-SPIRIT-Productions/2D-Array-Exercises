## Intro
In the previous exercise, we accessed elements in a list with unknown number of rows and columns.
For this exercise, we will create/edit 2D lists.

## List Comprehension
List comprehension is a syntactic construct that allows the creation of lists from existing iterables.  
For instance:
```py
foo = []
for i in range(11):
    foo.append(i)
foo2 = []
for i in range(11):
    foo2.append(i+3)
    
bar = [i for i in range(11)]
bar2 = [i+3 for i in range(11)]
```
`foo` will give the same results as `bar`; and `foo2` will give the same results as `bar2`.  

Working with existing collections:  
```py
foo = [
    "This",
    "is",
    "a",
    "sentence",
]
bar = [element+" " for element in foo]
```

## Exercise 3
In this exercise, we will mutate/instantiate 2D lists, using either nested for-loops or list comprehension.  

### Exercise 3a
Write a function `square_list` that returns a list that spans from 0 to (a given number -1 ) for each row, and having identical rows for (the given number - 1) number of columns.  
E.g. for a given number 3, the following will be returned:
```py
foo = [
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2],
]
```

### Exercise 3b
Write a function `triangular_list` that returns a list like follows:  
E.g. for a given number 2:
```py
foo = [
    [1, 2],
    [1, 2, 1, 2],
]
```
E.g. for a given number 3:
```py
foo = [
    [1, 2, 3],
    [1, 2, 3, 1, 2, 3],
    [1, 2, 3, 1, 2, 3, 1, 2, 3],
]
```

### Exercise 3c
Given 2 lists, write a function `cartesian` that does the following:
```py
x = ["x1", "x2", "x3", "x4"]  # list 1, given
y = ["y1", "y2", "y3", "y4"]  # list 2, given

result = [
    ["x1", "y1"]
    ["x2", "y2"]
    ["x3", "y3"]
    ["x4", "y4"]
]  # returned 2D list
```

### Exercise 3d
Write a function `process` that when given a 2D list, for every element, if the next element is an even value, increment the current element's value by 1.  
E.g.:
```py
input_list = [[1, 2, 3, 4, 5]]
output_list = [[2, 2, 4, 4, 5]]
```
