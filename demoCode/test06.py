import json

text = '{"3001": 128,"3012": 54}'
obj = json.loads(text)
print(f'obj : {obj}')
print(f"obj['3012'] : {obj['3012']}")

obj['2330'] = 600
text = json.dumps(obj)
print(f'text : {text}')