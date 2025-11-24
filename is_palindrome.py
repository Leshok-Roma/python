def is_palindrome(value):
    s = str(value).lower()
    s = s.replace(" ", "")
    return s == s[::-1]
