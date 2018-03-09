import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from utils import *

lines=open("probes.data").readlines()
cred = credentials.Certificate('hack101-b26f1b2127fd.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://hack101-46d94.firebaseio.com'
})

root = db.reference()
read_data = root.child('probe').get()
lat,lon = get_location()

for line in lines:
    data = line.split('\t')
    mac = data[1]
    name = data[2]
    signal_strength = data[4]

    try:
        get_data = read_data[str(mac)]
    except KeyError:
        pass
    if not hasattr(locals(), 'get_data') or get_data['signal'] < signal_strength:
        read_data[str(mac)] = {"name":name,"signal":signal_strength,"lat":lat, "lon":lon}

root.child('probe').set(read_data)
