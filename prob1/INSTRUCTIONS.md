## Intro
This series of exercise will focus on 2D lists in Python.  
The general concept is applicable to most other languages as well.  

## What are 2D List?
2D lists *or* two-dimensional lists are of the form `list of lists`.  
Imagine a table of data; if we put each row of the data into a list, and then proceed to put all these lists into one bigger list, then this resulting big list would represent the table of data in a 2D grid, rather than a typical single-dimensional list.  
```py
# Flat/1D/traditional lists
flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2D list
two_dimensional_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

For this exercise, consider a 3x3 2D-List. Here's what it looks like:  
```
(0, 0)   (0, 1)   (0, 2)  
(1, 0)   (1, 1)   (1, 2)  
(2, 0)   (2, 1)   (2, 2)
```  
*(Artist's representation)*  
Legend: Coordinates (x, y) => x is the row, and y is the column  
Note: In Python, indices start from 0.  
That is why the first element in a list has an index of 0.  

## How does this apply to Python?
We would represent it this way in code:  
```py
foobar = [
	[(0, 0), (0, 1), (0, 2)],
	[(1, 0), (1, 1), (1, 2)],
	[(2, 0), (2, 1), (2, 2)],
]
```
Alternatively, in a single line:
```py
foobar = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
```

To access a list element, we use the `[]` operator, e.g. foobar[0].  
When we perform `foobar[x]`, we are accessing the `(x-1)`-th element.  
Since each row is stored as a list inside the list foobar, this means that `foobar[x]` is the `(x-1)`-th row.
To access the inner list, we can continue to use the `[]` operator.  
Hence, `foobar[x+1][y+1]` corresponds to the `x`-th row and `y`-th column.  
E.g. `foobar[1][2]` will yield `(1,2)`, since 2nd row index is `1`, and 3rd column index is `2`.

## Real Example
Consider the following set of data on Microsoft Excel:  
![](https://i.imgur.com/J2VHFVM.png)  
We can represent the list using Python like so:
```python
excel_data = [
    [0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10, 11],
    [12, 13, 14, 15, 16, 17],
]
```
If we perform `excel_data[1][2]` we would get `8`.

## Exercise 1
There are a total of 3 sub-exercises in this module.  
You may find them in `exercise.py`.  
*The exact details can be found as comments in `exercise.py`.*  
For exercise 1a, you will be required to access a single element of a 2D list directly using indices.  
For exercise 1b and 1c, you will be required to access multiple elements of a 2D list, and make use of their values.

When you're done implementing all 3 functions in `exercise.py`, you can check your answers by running `check_solutions.bat`.  
You may simply double-click on it to have it run from Command Prompt.  
Alternatively to run it in *Windows Terminal + PowerShell*, you can `cd` to `prob1` and use: `.\check_solutions.bat`.

### Exercise 1a
Write a function `get_3_2(my_list)` that takes a 2D list `my_list` and returns
the element that is at the 3rd row, 2nd column.

### Exercise 1b
Consider a tic-tac-toe grid represented as a 2D-List. E.g.:  
```
X  O  X
O  X  O
X  O  X
```
Write a function `top_row_matches(tic_tac_toe)` that takes a 2D list `tic_tac_toe`, checks if
all 3 members of the top row match each other, and returns a boolean representing the results
(i.e. `True` or `False`).

E.g. Given the following grids, where `Ø` represents an arbitrary value in it's place:
```
# Grid 1
X X X
Ø Ø Ø
Ø Ø Ø

# Grid 2
X O X
Ø Ø Ø
Ø Ø Ø
```
Grid 1 should return `True`, while Grid 2 should return `False`.

### Exercise 1c
Consider the same tic-tac-toe grid.  
Write a function `left_to_right_matches(tic_tac_toe)` that takes a 2D list `tic_tac_toe`,
checks if the diagonal running from top left to bottom right has
all 3 members matching each other, and returns a boolean representing the results
(i.e. `True` or `False`).

E.g. Given the following grids, where `Ø` represents an arbitrary value in it's place:
```
# Grid 1
X Ø Ø
Ø X Ø
Ø Ø X

# Grid 2
X Ø Ø
Ø O Ø
Ø Ø X
```
Grid 1 should return `True`, while Grid 2 should return `False`.
