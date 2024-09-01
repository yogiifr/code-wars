# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

# Itteraton

def fake_bin(x):
    res = []
    
    for num in x:
        
        if int(num) < 5:
            res.append("0")
        else:
            res.append("1")
    
    return "".join(res)

# def fake_bin(x):
#     return "".join('0' if int(num) < 5 else '1' for num in x)