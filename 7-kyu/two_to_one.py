# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

# Union of sets
# Sorting
# String join

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
    # return ''.join(sorted(set(a1).union(set(a2))))

    # # Gabungkan dua string dan ambil karakter unik dengan set
    # unique_chars = set(s1).union(set(s2))
    
    # # Urutkan karakter dalam urutan abjad
    # sorted_chars = sorted(unique_chars)
    
    # # Gabungkan karakter menjadi string tunggal
    # result = ''.join(sorted_chars)