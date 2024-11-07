import re
import requests
import json


# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки

pattern = r'(?<=<h3>).*(?=</h3>)'

print(re.findall(pattern, text))

url = 'https://4pda.to//'
req_html = requests.get(url)
response = req_html.text

with open('4pda.html', 'w') as file:
    json.dump(response, file, indent=4)

print(re.findall(pattern,response))
