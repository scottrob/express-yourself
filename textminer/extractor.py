import re

def phone_numbers(test):
    return re.findall(r'\d?\(?\d{3}\)?\s?\d{3}-?\d{4}' ,test)
