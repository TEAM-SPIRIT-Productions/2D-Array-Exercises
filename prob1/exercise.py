# This series of exercise will focus on 2D lists in Python.
# The general concept is applicable to most other languages as well.
#
# For this exercise, consider a 3x3 2D-List. Here's what it looks like:
# (0, 0)   (0, 1)   (0, 2)
# (1, 0)   (1, 1)   (1, 2)
# (2, 0)   (2, 1)   (2, 2)
# (Artist's representation)
# Legend: (x, y) => x is the row, and y is the column
# Note: In Python, indices start from 0.
# That is why the first element in a list has an index of 0.
#
# We would represent it this way in code:
# foobar = [
# 	[(0, 1), (0, 2), (0, 3)],
# 	[(1, 1), (1, 2), (1, 3)],
# 	[(2, 1), (2, 2), (2, 3)],
# ]
# Alternatively, in a single line:
# foobar = [[(0, 1), (0, 2), (0, 3)], [(1, 1), (1, 2), (1, 3)], [(2, 1), (2, 2), (2, 3)]]
#
# To access a list element, we use the [] operator, e.g. foobar[0]
# When we perform foobar[x], we are accessing the (x-1)-th element.
# Since each row is stored as a list inside of the list foobar,
# this means that foobar[x] is the (x-1)-th row.
# To access the inner list, we can continue to use the [] operator.
# Hence, foobar[x+1][y+1] corresponds to the x-th row and y-th column
# E.g. foobar[1][2] will yield (1,2)


# In this exercise, you are required to access elements of the list.
# Write a function get_3_2 that takes a 2D list (my_list) and returns
# the element that is at the 3rd row, 2nd column
def get_3_2(my_list):
	# You code goes here
	element = 0
	return element


# Consider a tic-tac-toe grid represented as a 2D-List. E.g.:
# X  O  X
# O  X  O
# X  O  X
# Write a function top_row_matches that takes a 2D list (tic_tac_toe), checks if
# all 3 members of the top row match each other, and returns a boolean
# (i.e. True or False)
def top_row_matches(tic_tac_toe):
	matches = False
	# You code goes here
	return matches


# Consider the same tic-tac-toe grid.
# Write a function left_to_right_matches that takes a 2D list (tic_tac_toe),
# checks if the diagonal running from top left to bottom right has
# all 3 members matching each other, and returns a boolean
# (i.e. True or False)
def left_to_right_matches(tic_tac_toe):
	matches = False
	# You code goes here
	return matches
