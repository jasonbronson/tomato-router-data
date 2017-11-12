#!/usr/bin/python
import re
import json 
import requests
import myenv
#import redis
from hurry.filesize import size

def get_device_list(host, username, password, http_id):
    req = requests.post('http://{}/update.cgi'.format(host),
                        data={'_http_id':http_id, 'exec':'devlist'},
                        auth=requests.auth.HTTPBasicAuth(username, password))
    #get ip list 
    data = {param: json.loads(value.replace("\'",'\"'))
             for param, value in re.findall(r"(?P<param>\w*) = (?P<value>.*);", req.text)
             if param != "dhcpd_static"}
 
    req = requests.get('http://{}/wireless.jsx?_http_id={}'.format(host, http_id),
                        auth=requests.auth.HTTPBasicAuth(username, password))
 
    data.update({param: json.loads(value.replace("'",'"'))
                    for param, value in re.findall(r"(?P<param>\w*) = (?P<value>.*);", req.text)
                    if param != 'u'})
 
    return data
 
def get_log(host, username, password, http_id):
    req = requests.get('http://{}/logs/view.cgi?which=100&_http_id={}'.format(host, http_id),
                        auth=requests.auth.HTTPBasicAuth(username, password))
    data = req.text;
    return data

def get_bandwidth(host, username, password, http_id):
    req = requests.post('http://{}/update.cgi'.format(host),
                        data={'exec':'iptraffic','_http_id':http_id},
                        auth=requests.auth.HTTPBasicAuth(username, password))
    data = req.text;
    data = format_bandwidth_data(data)
    return data

def format_bandwidth_data(data):
    #format data dynamically
    exec(data)
    #r = redis.StrictRedis(host=myenv.redishost, port=6379, db=0)
    #Host	Download (bytes/s)	Upload (bytes/s)	TCP IN/OUT (pkt/s)	UDP IN/OUT (pkt/s)	ICMP IN/OUT (pkt/s)	TCP Connections	UDP Connections
    
    header = 'host,', 'download,', 'upload,', 'total bandwidth';
    #csv format
    #print header
    jsonList=[header]
    for item in iptraffic:
        host = item[0]
        download = item[1]
        upload = item[2]
        tcp = item[3]
        udp = item[4]
        icmp = item[5]
        tcpconn = item[6]
        udpconn = item[7]

        #setup redis save here
        #r.set('host', host)
        
        #csv format
        #print '{}, {}, {}, {}'.format(host, size(download), size(upload), totalbandwidth)
    
        totalbandwidth = size(download + upload)
        itemList=[host, size(download), size(upload), totalbandwidth]
        jsonList.append(itemList)   
        
    return json.dumps(jsonList)


#example get device list
#print get_device_list(myenv.ip, myenv.username, myenv.password, myenv.httpid)

#print logs example
#print get_log(myenv.ip, myenv.username, myenv.password, myenv.httpid)

#print bandwidth example as json format
print get_bandwidth(myenv.ip, myenv.username, myenv.password, myenv.httpid)



