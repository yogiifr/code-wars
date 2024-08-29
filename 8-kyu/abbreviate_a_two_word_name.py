# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

# String Manipulation
# Indexing: Mengakses karakter dalam string dengan menggunakan indeks.
# String Slicing: Mengambil bagian dari string menggunakan slicing.
# String Methods: Metode seperti .split(), .upper() untuk memanipulasi string.

# String Splitting
# .split() Method: Memisahkan string berdasarkan spasi menjadi list kata-kata.

def abbrev_name(name):
    nama = name.split()
    initialDepan = nama[0][0].upper()
    initialBelakang = nama[1][0].upper()

    return f"{initialDepan}.{initialBelakang}"