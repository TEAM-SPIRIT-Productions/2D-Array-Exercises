"""Unit Test for Exercise 3

@author KOOKIIE
This set of unit tests will check if the code written in exercise.py
is indeed correct.
"""
import pytest
import exercise


square_4 = [
	[0, 1, 2, 3],
	[0, 1, 2, 3],
	[0, 1, 2, 3],
	[0, 1, 2, 3],
]


square_5 = [
	[0, 1, 2, 3, 4],
	[0, 1, 2, 3, 4],
	[0, 1, 2, 3, 4],
	[0, 1, 2, 3, 4],
	[0, 1, 2, 3, 4],
]


triangular_3 = [
	[1, 2, 3],
	[1, 2, 3, 1, 2, 3],
	[1, 2, 3, 1, 2, 3, 1, 2, 3],
]


triangular_4 = [
	[1, 2, 3, 4],
	[1, 2, 3, 4, 1, 2, 3, 4],
	[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
	[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
]


cartesian_x_1 = [1, 2, 3, 4, 5]
cartesian_y_1 = [6, 7, 8, 9, 10]
cartesian_result_1 = [
	[1, 6],
	[2, 7],
	[3, 8],
	[4, 9],
	[5, 10],
]


cartesian_x_2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
cartesian_y_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
cartesian_result_2 = [
	["0", "a"],
	["1", "b"],
	["2", "c"],
	["3", "d"],
	["4", "e"],
	["5", "f"],
	["6", "g"],
	["7", "h"],
	["8", "i"],
	["9", "j"],
	["10", "k"],
]


input_list_1 = [[1, 2, 3, 4, 5]]
output_list_1 = [[2, 2, 4, 4, 5]]


input_list_2 = [
	[3, 7, 12, 76, 1, 65, 72, 63],
	[6, 3, 136, 3, 7, 546, 8, 4],
	[1, 2, 8, 5, 1, 876, 4, 45],
]
output_list_2 = [
	[3, 8, 13, 76, 1, 66, 72, 63],
	[6, 4, 136, 3, 8, 547, 9, 4],
	[2, 3, 8, 5, 2, 877, 4, 45],
]


@pytest.mark.parametrize("number, expected", [
	(4, square_4),
	(5, square_5),
])
def test_square_list(number, expected):
	assert exercise.square_list(number) == expected


@pytest.mark.parametrize("number, expected", [
	(3, triangular_3),
	(4, triangular_4),
])
def test_triangular_list(number, expected):
	assert exercise.triangular_list(number) == expected


@pytest.mark.parametrize("input_1, input_2, expected", [
	(cartesian_x_1, cartesian_y_1, cartesian_result_1),
	(cartesian_x_2, cartesian_y_2, cartesian_result_2),
])
def test_cartesian(input_1, input_2, expected):
	assert exercise.cartesian(input_1, input_2) == expected


@pytest.mark.parametrize("input_list, expected", [
	(input_list_1, output_list_1),
	(input_list_2, output_list_2),
])
def test_process(input_list, expected):
	assert exercise.process(input_list) == expected
