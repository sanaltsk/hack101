import json
import requests
import commands
import pprint

def get_WAPs():
    pp = pprint.PrettyPrinter(indent=4)
    access_points = commands.getstatusoutput('sudo iw wlan0 scan | egrep "^BSS|signal:|: channel"')[1].split('\n')
    pp.pprint(access_points)
    wifiAccessPoints = []
    i = 0
    while i < len(access_points):
        if access_points[i][0:3] != 'BSS':
            i = i+1
            continue
        macAddress = access_points[i][4:21]
        signalStrength = access_points[i+1].split(' ')[1]
        channel = access_points[i+2].split(' ')[-1]
        wifiAccessPoint = {'macAddress':macAddress, 'signalStrength':signalStrength, 'channel':channel}
        pp.pprint(wifiAccessPoint)
        wifiAccessPoints.append(wifiAccessPoint)
        i= i+3
    return wifiAccessPoints

def get_location():
    private_key = 'AIzaSyCqp1Rwd_jVwqq0yMXEQLGI41719lzslsI'
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + private_key
    headers = {'content-type': 'application/json'}
    wifiAccessPoints = get_WAPs()
    payload = {'considerIp':'true', 'wifiAccessPoints':wifiAccessPoints}
    jsonPayload=json.dumps(payload)
    r = requests.post(url,data=jsonPayload,headers = headers)
    response = json.loads(r.text)
    return (response['location']['lat'], response['location']['lng'])
