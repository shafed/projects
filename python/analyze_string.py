def analyze_string(s):
    return {
        "length": len(s),
        "words": len(s.split()),
        "digits": sum(i.isdigit() for i in s),
        "upper": sum(i.isupper() for i in s),
        "lower": sum(i.islower() for i in s),
    }


s = input()
res = analyze_string(s)
print(res)
