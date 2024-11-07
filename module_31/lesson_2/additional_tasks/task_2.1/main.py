from __future__ import annotations
import re

text = 'Было закуплено 12 единиц техники по 410 рублей.'

def trip_maney(m: re.Match) -> str:
    print(m.group())
    return str(float(m[0]) ** 3)


pattern = r'(?:\d+)'

print(re.sub(pattern, trip_maney, text))
