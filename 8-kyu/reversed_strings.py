# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# String slicing [start:stop:step] terus dikasih negative indexing jadinya kek gini [::-1] mundur ntar dia baca stringnya

def solution(string):
    return string[::-1]