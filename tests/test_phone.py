import pytest
from phone_utils import normalize_phone


def test_valid_plus977_number():
    assert normalize_phone("+9779769366977") == "+9779769366977"


def test_valid_zero_start_number():
    assert normalize_phone("09769366977") == "+9779769366977"


def test_valid_10_digit_number():
    assert normalize_phone("9769366977") == "+9779769366977"
#invalid test cases
#1 short number 
def test_invalid_short_number():
    with pytest.raises(ValueError):
        normalize_phone("98123456")

#wrng country code
def test_invalid_country_code():
    with pytest.raises(ValueError):
        normalize_phone("+9789769366977")

#alphabetic character
def test_invalid_characters():
    with pytest.raises(ValueError):
        normalize_phone("97ABC45677")



#EDGE TEST cases
def test_number_with_spaces_and_dashes():
    assert normalize_phone("97-69 36-69 77") == "+9779769366977"


def test_edge_wrong_start_digits():
    with pytest.raises(ValueError):
        normalize_phone("9612345678")