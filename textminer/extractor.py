import re

def phone_numbers(test):
    return re.findall(r'\(?\d{3}.?.?\d{3}.?\d{4}' ,test)
