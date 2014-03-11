# ex 5
import json
import requests

r = requests.get('http://ialpython.apiary.io/laboratories')
lab = json.loads(r.content)

print '\n Laboratori con rete down:\n\n'

for p in lab:
    if p['network_status'] == 'down':
        print p['name']



print '\n'