"""Unit Test for Exercise 4

@author KOOKIIE
This set of unit tests will check if the code written in exercise.py
is indeed correct.
"""
import pytest
import exercise


given_list_1 = [1, 2, 3]
return_list_1 = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]


given_list_2 = [1, 2, 3, 4]
return_list_2 = [
	(1, 1), (1, 2), (1, 3), (1, 4),
	(2, 2), (2, 3), (2, 4),
	(3, 3), (3, 4),
	(4, 4)
]


@pytest.mark.parametrize("input_list, expected", [
	(given_list_1, return_list_1),
	(given_list_2, return_list_2),
])
def test_scalar_product(input_list, expected):
	assert exercise.scalar_product(input_list) == expected
