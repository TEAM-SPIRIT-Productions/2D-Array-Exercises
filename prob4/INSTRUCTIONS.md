## Intro
In the previous exercise, we created/edited 2D lists.  
For this exercise, we will move to applying previously learnt techniques to novel situations.  

## Nested For-loops 
Consider a situation where, for every element in a 1D list, you need to apply a mathermatical operator to every element of the list.  
The way that we would use for-loops inside of for-loops to do so is not dissimilar to the way we navigate 2D lists.  
E.g. Given a list `[1, 2, 3, 4, 5]`, we want a list that contains sums of elements with other elements. That is,
for every element, we want the sum of itself and 1 other element of the list, and we would like to capture all permutations.  
This would give us an output that looks something like this:
```py
[(1+2), (1+3), (1+4), (1+5), (2+1), (2+3), (2+4), (2+5), (3+1), ...]
```

By using a for-loop inside of a for-loop, we can *treat* the given list as follows:
```py
[
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5],
]
```
*Note: This is only a visualisation tool*

Outer-loop (rows): Imagine transversing from the top left to bottom right of the grid; we go from 1 to 5 like below:  
*Note: The symbol Ø denotes unimportant regions*
  ```py
[
    [1, Ø, Ø, Ø, Ø],
    [Ø, 2, Ø, Ø, Ø],
	[Ø, Ø, 3, Ø, Ø],
	[Ø, Ø, Ø, 4, Ø],
	[Ø, Ø, Ø, Ø, 5],
]
  ```
Inner-loop (columns): Imagine transversing from left-most to right-most element in a row: `[1, 2, 3, 4, 5]`  

Solution:
```py
def permutate(some_list):
	output = []
	for row in some_list:
		for column in some_list:
			result = row + column
			output.append(result)
	return output
```

## Exercise 4
For this exercise, we would like to obtain all possible scalar product combinations of any 2 elements in a list.  
Hence write a function `scalar_product` that, given a list of real numbers, returns an ordered list of tuples representing such combinations (nC2).  
E.g.:
```py
given_list = [1, 2, 3]
return_list = [
    (1, 1), (1, 2), (1, 3), 
    (2, 2), (2, 3), 
    (3, 3)
]
```
Note: Scalar products are commutative. That is, *a × b = b × a*.  
Hence, (1, 2) is equivalent to (2, 1) in this context - which is why we do not list (2, 1), (3, 1), etc.
