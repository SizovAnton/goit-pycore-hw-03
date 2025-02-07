import re

def normalize_phone(phone_number):
  pattern = r'\D'
  replacement = r''

  formatted_phone = re.sub(pattern, replacement, phone_number).strip()

  if formatted_phone.startswith('0'):
        formatted_phone = '380' + formatted_phone[1:]
  elif formatted_phone.startswith('80'):
        formatted_phone = '380' + formatted_phone[2:]
  elif formatted_phone.startswith('380'):
      pass

  return '+' + formatted_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
  
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)