import json
json_file = '''
{
    "module": "blestsploit"    
}
'''
js = json.loads(json_file)
for i in js:
    print(i)

