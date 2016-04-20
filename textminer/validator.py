import re

def binary(string):
    return re.match(r'^[0-1]+$',string)

def binary_even(string):
    return re.match(r'^[0-1]+?[0]$', string)

def hex(string):
    return re.match(r'^[A-Fa-f0-9]+$',string)

def word(string):
    return re.match(r'^[0-9]*[\-A-Za-z]+$',string)

def words(string):
    matches = re.findall(r'^[0-9]*?[\-A-Za-z]+$',string)
    return len(matches)

def phone_number(string):
    return re.match(r'\(?\d{3}.?.?\d{3}.?\d{4}' ,string)

def money(string):
    return re.match(r'^\$(\d*)(,\d{3}?)*(\.\d{2})?')
