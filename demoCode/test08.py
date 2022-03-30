import urllib.parse as UP

text = '新冠肺炎'

print(f'UP.quote(text) : {UP.quote(text)}')

text = '%E7%96%AB%E8%8B%97'
print(f'UP.unquote(text) : {UP.unquote(text)}')