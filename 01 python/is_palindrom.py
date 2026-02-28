def is_palindrom(s: str) -> bool:
    d = "".join(c.lower() for c in s if c.isalnum())
    return d == d[::-1]


s = input()
res = is_palindrom(s)
print(res)
