def uppercase_letters(s):
    for c in s: 
        yield c.upper()

uppercase_letters('abcdefgh')