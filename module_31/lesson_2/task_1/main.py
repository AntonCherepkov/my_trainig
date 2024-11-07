import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

pattern = r'\b[aeiouy]\w+'
print(re.findall(pattern, text, flags=re.IGNORECASE))

pattern = r'\b[^aeiouy\W\s]\w+'
print(re.findall(pattern, text, flags=re.IGNORECASE))
