# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to
# uppercase letters and vice versa.
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Function Description
# Complete the swap_case function in the editor below.
# swap_case has the following parameters:
# string s: the string to modify
# Returns
# string: the modified string
# Input Format
# A single line containing a string .
# Constraints
# Sample Input 0
# HackerRank.com presents "Pythonist 2".
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def str_vice_versa(x):
    y=""
    for char in x:
        if char == char.lower():
            y=y+char.upper()
        elif char ==char.upper():
            y=y+char.lower()
        else:
            y=y+char
    return y




x="Pythonist 2"
print(str_vice_versa(x))