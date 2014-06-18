import json, requests, a_c

USB_name='/dev/ttyACM0'
url = 'http://192.241.133.179:22222/api'
prev_time=0
curr_time=0
curr_punch=''


"""print data
print data['items'][0]['commands']
print data['items'][0]['commands'][0][0].encode('ascii')
"""


ser=a_c.setup(USB_name)
while True:
    
    
    resp = requests.get(url)
    d = json.loads(resp.text)
    list_punches=[]
    list_list_punches=d['items'][0]['commands']
    if len(list_list_punches)>0:
        for l in list_list_punches:
            list_punches.append(l)
        list_punches.sort()
        prevprev = prev_time
        for l in list_punches:
            if prev_time<l[0]:
                prev_time=l[0]
                curr_punch=l[1].encode('ascii')
                break
        if prevprev!=prev_time:
            a_c.punch(ser,curr_punch)

    
