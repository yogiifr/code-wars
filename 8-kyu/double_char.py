# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Looping itteration lagi

def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res