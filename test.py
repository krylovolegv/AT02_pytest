import pytest
from main import sort_list  # замените my_module на имя вашего модуля

def test_sort_list_ascending():
   assert sort_list([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]

def test_sort_list_descending():
   assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_list_mixed():
   assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]

@pytest.mark.parametrize("numbers, expected", [
   ([7, 2, 5, 3], [2, 3, 5, 7]),
   ([10, -10, 0], [-10, 0, 10]),
   ([], []),
   ([1], [1])
])
def test_sort_list_parametrized(numbers, expected):
   assert sort_list(numbers) == expected

# from main import is_palindrome  # замените my_module на имя вашего модуля
#
# def test_is_palindrome_true():
#    assert is_palindrome("madam") == True
#
# def test_is_palindrome_false():
#    assert is_palindrome("hello") == False
#
# @pytest.mark.parametrize("s, expected", [
#    ("racecar", True),
#    ("python", False),
#    ("level", True),
#    ("", True),  # Пустая строка является палиндромом
# ])
# def test_is_palindrome_parametrized(s, expected):
#    assert is_palindrome(s) == expected

# from main import check
#
# def test_check():
#    assert check(6) == True
#
# def test_check2():
#    assert check(3) == False
#
# @pytest.mark.parametrize("number, expected", [
#    (2, True),
#    (5, False),
#    (0, True),
#    (56, True),
#    (-3, False)
# ])
# def test_check_with_param(number, expected):
#    assert check(number) == expected
