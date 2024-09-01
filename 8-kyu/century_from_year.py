# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28

# Integer Division // jadi kek 1900 dikurang jadi 1899 dibagi 100 jadi 18 + 1 jadinya 19
# Contoh lain, buat tahun dibawah 100 jadi 0 terus tambah 1, jadinya abad ke 1
# Kalo tahun 234, dikurang 1 jadi 233 tetep di range abad 3 karena integer division jadi 2, ditambah 1 jadi 3

def century(year):
    return (year - 1) // 100 + 1