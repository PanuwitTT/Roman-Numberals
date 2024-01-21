# 64364757ภาณุวิชญ์ ขวัญเพ็ง
import pytest
# standard
from numberal.roman import to_roman
#____________________________________________________________________________________________________


def test_calling_function():
    """call a roman numberal"""
    
@pytest.mark.parametrize(
    "arabic_num,roman_num",
    [
       # base case
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
        # Add case
        (2, "II"),
        (3, "III"),
        
        # Sub csse
        (4, "IV"),
        (9, "IX"),
        (40, "XL"),
        (90, "XC"),
        (400, "CD"),
        (900, "CM"),
        # Other cases
        (3549, "MMMDXLIX"),
        (2754, "MMDCCLIIII"),
        (3999, "MMMCMXCIX"),
    ]
)
def test_roman_numerals_conversion(arabic_num, roman_num):
    # Your testing logic here
    pass