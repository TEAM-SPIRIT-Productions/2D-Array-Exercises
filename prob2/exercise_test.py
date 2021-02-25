"""Unit Test for Exercise 2

@author KOOKIIE
This set of unit tests will check if the code written in exercise.py
is indeed correct.
"""
import pytest
import exercise

first_3_by_3 = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
]

second_3_by_3 = [
	[9, 8, 7],
	[6, 5, 4],
	[3, 2, 1],
]

third_3_by_3 = [
	[1234, 75, 23],
	[6243, 65, 12],
	[7, 234, 87],
]

five_by_five = [
	[132, 54, 76, 52, 2],
	[56, 75, 22, 65, 12],
	[256, 19, 2, 83, 5],
	[7, 53, 17, 634, 34],
	[8, 36, 25, 13, 41],
]


@pytest.mark.parametrize("input_list, expected", [
	(first_3_by_3, 2),
	(second_3_by_3, 16),
	(third_3_by_3, 1257),
	(five_by_five, 210)
])
def test_sum_even_elements_in_first_row(input_list, expected):
	assert exercise.sum_even_elements_in_first_row(input_list) == expected


@pytest.mark.parametrize("input_list, expected", [
	(first_3_by_3, 24),
	(second_3_by_3, 30),
	(third_3_by_3, 7606),
	(five_by_five, 695)
])
def test_sum_even_elements(input_list, expected):
	assert exercise.sum_even_elements(input_list) == expected


@pytest.mark.parametrize("input_list, expected", [
	(first_3_by_3, 756),
	(second_3_by_3, 2160),
	(third_3_by_3, 2761182720),
	(five_by_five, 2430911607000)
])
def test_product_of_sum(input_list, expected):
	assert exercise.product_of_sum(input_list) == expected


@pytest.mark.parametrize("input_list, expected", [
	(first_3_by_3, 8),
	(second_3_by_3, 10),
	(third_3_by_3, 6255),
	(five_by_five, 148)
])
def test_sum_of_oddeven(input_list, expected):
	assert exercise.sum_of_oddeven(input_list) == expected
