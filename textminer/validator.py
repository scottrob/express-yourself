import re

def binary(string):
    return re.match(r'^[0-1]+$',string)

def binary_even(string):
    return re.match(r'^[0-1]+?[0]$', string)

def hex(string):
    return re.match(r'^[A-Fa-f0-9]+$',string)

def word(string):
    return re.search(r'^[\-A-Za-z18]+$',string)

def 
