import pytest
import pytest
from main import is_palindrome  # замените my_module на имя вашего модуля

def test_is_palindrome_true():
   assert is_palindrome("madam") == True

def test_is_palindrome_false():
   assert is_palindrome("hello") == False

@pytest.mark.parametrize("s, expected", [
   ("racecar", True),
   ("python", False),
   ("level", True),
   ("", True),  # Пустая строка является палиндромом
])
def test_is_palindrome_parametrized(s, expected):
   assert is_palindrome(s) == expected

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
