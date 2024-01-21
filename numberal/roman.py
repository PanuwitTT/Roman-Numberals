# 64364757ภาณุวิชญ์ ขวัญเพ็ง

class NumberOutOfRange(Exception):

  def __init__(self, message="เลขอารบิกที่ส่งเข้ามาอยู่นอกช่วงของเลขโรมัน"):
    super().__init__(message)

  def get_message(self):
    return self.message

def to_roman(arabic_num):


  if not isinstance(arabic_num, int) or arabic_num < 1 or arabic_num > 3999:
    raise NumberOutOfRange()

  roman_numerals = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
  }

  roman_num = ""
  for i in range(len(roman_numerals) - 1, -1, -1):
    while arabic_num >= roman_numerals[i]:
      roman_num += roman_numerals[i]
      arabic_num -= roman_numerals[i]

  return roman_num