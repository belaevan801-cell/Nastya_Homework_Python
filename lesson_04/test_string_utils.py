import pytest
from string_utils import StringUtils


string_utils = StringUtils()

-- 1


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),


])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("None", "None"),

])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


-- 2


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
  (" skypro", "skypro"),
  (" ", ""),
  (" python", "python"),
  (" java", "java"),
  (" windows", "windows"),
  (" ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    (" ", ""),
    ("04 апреля 2023", "04 апреля 2023"),
    ("12345", "12345")

])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


-- 3


@pytest.mark.positive
@pytest.mark.parametrize("str1, str2, result", [
    ("Skypro", "o", True),
    ("Skypro", "ro", True),
    ("Skypro", "pro", True),
    ("Skypro", "S", True),
    ("Skypro", "r", True),
    ("Skypro", "k", True)


])
def test_contains_positive(str1, str2, result):
    string_utils = StringUtils()
    res = string_utils.contains(str1, str2)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize("str1, str2, result", [
    ("Skypro", "a", False),
    ("Skypro", "ra", False),
    ("Skypro", "Str", False),
    ("Skypro", "D", False),
    ("Skypro", "T", False),
    ("Skypro", "z", False)

])
def test_contains_negative(str1, str2, result):
    string_utils = StringUtils()
    res = string_utils.contains(str1, str2)
    assert res == result


--4


@pytest.mark.positive
@pytest.mark.parametrize("input_text, input_symbol, expected_output", [
    ("Text", "T", "ext"),
    ("Text", "t", "Tex"),
    ("12345", "3", "1245"),
    ("12345", "45", "123"),


])
def test_delete_symbol_positive(input_text, input_symbol, expected_output):
    my_text = StringUtils()
    assert my_text.delete_symbol(input_text, input_symbol) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize("input_text, input_symbol, expected_output", [
    ("Text", "f", "Text"),
    ("Text", "m", "Text"),
    ("12345", "9", "12345"),
    ("12345", "78", "12345"),
    ("test string", "z", "test string"),
    ("", "d", ""),
    (" ", "d", " "),
    ("text", "", "text")

])
def test_delete_symbol_negative(input_text, input_symbol, expected_output):
    my_text = StringUtils()
    assert my_text.delete_symbol(input_text, input_symbol) == expected_output
