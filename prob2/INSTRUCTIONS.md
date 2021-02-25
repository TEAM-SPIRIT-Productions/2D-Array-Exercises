## Intro
In the previous exercise, we accessed elements of a 2D list (of known size/dimensions) by directly referencing indices.  
For this exercise, we will attempt to access elements in a list with unknown numbers of rows and columns.

## List Transversal
Foreach loops are control flow statements that do not require explicit counters to transverse items in a collection.  
This is considered the idiomatic way of using for-loops in Python.  

Consider a list of Strings `foobar`:
```py
foobar = [
    "Lorem ipsum dolor sit amet"
    "consectetur adipiscing elit"
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    "Ut enim ad minim veniam"
    "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
    "Excepteur sint occaecat cupidatat non proident"
    "sunt in culpa qui officia deserunt mollit anim id est laborum."
]
```
Let's say we wish to convert all the strings to lowercase. We would simply do the following:
```py
for line in foobar:
    line.lower()
```

Notice that we did not need to specify counters, unlike in other languages, say Java 8:
```java
for (int i=0; i<foobar.size(); i++) {
    foobar[i].toLowerCase();
}
```

However, there may be times when we require the indices of elements. How should we proceeed then?  
Enter the `enumerate()` function.  
Let's say we would like to concatenate the value of `index + 2` to the end of each element in `foobar`, but only if it is a multiple of 3:

```py
for index, line in enumerate(foobar):
	if index%3:  # non-zero values are truthy - they evaluate to True in boolean contexts
		line += str(index + 2)
```

## Exercise 2
Given the techniques we've learnt in Exercise 1, not too much additional information should be needed to complete Exercise 2.  
Note that to check if a number is even, we can perform `number % 2`; if the result is 0, it is even.

### Exercise 2a
Write a function `sum_even_elements_in_first_row` that returns the sum of all even-index elements in the first row of a 2D list `unknown_list`.  

### Exercise 2b
Write a function `sum_even_elements` that returns the sum of all even-index elements in all rows of a 2D list `unknown_list`.

### Exercise 2c
Write a function `product_of_sum` that returns the product of the sums of each row, for a 2D list `unknown_list`.  
E.g. for the following list:
```python
unknown_list = [
    [1, 2],
    [3, 4],
    [5, 6],
]
```
You would need to return the value of `(1+2) * (3+4) * (5+6)`.

### Exercise 2d
Write a function `sum_of_oddeven` that returns the sum of elements with odd row, but even column indices, given a 2D list `unknown_list`. 
E.g. for the following list:
```python
unknown_list = [
    [1, 2, 3],  # Row 0; 0 is considered even in computing
    [4, 5, 6],
    [7, 8, 9],
]
```
The elements `4` and `6` are the only elements with odd row, but even column indices. 
