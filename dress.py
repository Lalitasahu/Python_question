import json
from webbrowser import open_new
x= json.loads(open('dress.json','r').read())
dictionary={}
l=[]
for i in x['products']:
    l.append({'code':i['code'],
    'fnlColorVariantData':i['fnlColorVariantData'],
    'name':i['name'],'brickName':i['brickName'],
    'price':i['price'],'url':i['url']})
    # print(l)

# print(x['products'][0].keys())
# max=x['products'][0]['code']
# for i in x['products']:
#     if i['code']>max:                       
#         max=i['code']
# print(max)
# print(x['products'][0].keys())
for i in x['products']:
    print(i)
       
with open('dress_output.json','w') as file:
    file.write(json.dumps(l,indent=4,sort_keys=True))
    print(len(l))


