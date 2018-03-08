import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
import json

def location():
  send_url = 'http://freegeoip.net/json'
  r = requests.get(send_url)
  j = json.loads(r.text)
  lat = j['latitude']
  lon = j['longitude']
  return lat,lon


lines=open("log.txt").readlines()
cred = credentials.Certificate('hack101-b26f1b2127fd.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://hack101-46d94.firebaseio.com'
})

root = db.reference()

push_data = {}
count = 0
for line in lines:
    data = line.split('\t')
    mac = data[1]
    name = data[2]
    lat,lon = location()
    singnal_strength = data[4]

    print(mac+":" + name+":"+singnal_strength)

    if mac not in push_data:
        push_data[mac] = {"name":name,"signal":singnal_strength,"lat":lat, "lon":lon}
        probe_data = root.child('probe').child(str(mac)).set(push_data[mac])
        count+=1

# print(push_data)
# result = db.reference('users').get()

