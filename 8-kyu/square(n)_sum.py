# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# looping iteration

def square_sum(numbers):
    res=0
    for key in numbers:
        res+=key**2
    return res