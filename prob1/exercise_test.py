"""Unit Test for Exercise 1

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

ttt_1 = [
	["O", "X", "X"],
	["O", "O", "X"],
	["X", "O", "X"],
]

ttt_2 = [
	["X", "X", "X"],
	["O", "O", "O"],
	["X", "O", "X"],
]

ttt_3 = [
	["X", "O", "X"],
	["X", "X", "O"],
	["O", "O", "X"],
]


@pytest.mark.parametrize("input_list, expected", [
	(first_3_by_3, 7),
	(second_3_by_3, 2),
	(third_3_by_3, 234)
])
def test_get_3_2(input_list, expected):
	assert exercise.get_3_2(input_list) == expected


@pytest.mark.parametrize("input_list, expected", [
	(ttt_1, False),
	(ttt_2, True),
	(ttt_3, False)
])
def test_top_row_matches(input_list, expected):
	assert exercise.top_row_matches(input_list) == expected


@pytest.mark.parametrize("input_list, expected", [
	(ttt_1, False),
	(ttt_2, False),
	(ttt_3, True)
])
def test_left_to_right_matches(input_list, expected):
	assert exercise.left_to_right_matches(input_list) == expected
