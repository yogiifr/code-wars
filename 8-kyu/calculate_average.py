# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

# Conditional Check (Empty List)
# Summing Elements (list) - Average with total lenght of number (len)

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        total = sum(numbers)
        average = total / len(numbers)
        return average