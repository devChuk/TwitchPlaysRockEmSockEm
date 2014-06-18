import json, requests

url = 'http://0.0.0.0:22222/api'

resp = requests.get(url)
d = json.loads(resp.text)

"""print data
print data['items'][0]['commands']
print data['items'][0]['commands'][0][0].encode('ascii')
"""

list_punches=[]
list_list_punches=d['items'][0]['commands']
for l in list_list_punches:
    list_punches.append(l[0].encode('ascii'))
    
