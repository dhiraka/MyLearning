def reverse_string(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


def is_palindrome(st):
    s = ''.join(e for e in st if e.isalnum())
    if s == reverse_string(s):
        return True
    return False


print is_palindrome("baba")
print is_palindrome("babab")
