"""-------------2-------------"""
d = {
'a': 1,
'b': 2,
'c': 3,
'd': 4,
'e': 5,
'f': 6
}


def reversed_print(dct: dict):
    """Print reversed values of dict."""
    values = list(dct.values())
    values.sort(reverse=True)
    print(values)


# reversed_print(d)
"""------------3--------------"""


def progression(N):
    multiplier = 0
    for n in range(N):
        multiplier += 2**n
    return 1 + 5 * multiplier


# print(progression(3))
"""------------4----------------"""

my_dict = {
    '1': 1,
    '2': 2,
    '3': 3
}
print(max(my_dict.values()))
