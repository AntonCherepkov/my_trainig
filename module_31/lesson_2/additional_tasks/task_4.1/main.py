import re

text_1 = """Вечер за окном.
/Ещё один день прожит./
Жизнь скоротечна..."""

# TODO: Здесь надо пилить и пилить и пилить... 

pattern = r'([^аоуеёиыэюя\W\s]*?[аоуеёиыэюя][^аоуеёиыэюя\W\s]*?)/'

print(re.findall(pattern, text_1, flags=re.IGNORECASE))
