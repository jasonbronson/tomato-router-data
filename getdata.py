#!/usr/bin/python
import re
import json 
import requests
import myenv
#import redis
from hurry.filesize import size

def get_device_list(ROUTER_IP, ROUTER_USERNAME, ROUTER_PASSWORD, HTTP_ID):
    req = requests.post('http://{}/update.cgi'.format(ROUTER_IP),
                        data={'_HTTP_ID':HTTP_ID, 'exec':'devlist'},
                        auth=requests.auth.HTTPBasicAuth(ROUTER_USERNAME, ROUTER_PASSWORD))
    #get ip list 
    data = {param: json.loads(value.replace("\'",'\"'))
             for param, value in re.findall(r"(?P<param>\w*) = (?P<value>.*);", req.text)
             if param != "dhcpd_static"}
 
    req = requests.get('http://{}/wireless.jsx?_HTTP_ID={}'.format(ROUTER_IP, HTTP_ID),
                        auth=requests.auth.HTTPBasicAuth(ROUTER_USERNAME, ROUTER_PASSWORD))
 
    data.update({param: json.loads(value.replace("'",'"'))
                    for param, value in re.findall(r"(?P<param>\w*) = (?P<value>.*);", req.text)
                    if param != 'u'})
 
    return data
 
def get_log(ROUTER_IP, ROUTER_USERNAME, ROUTER_PASSWORD, HTTP_ID):
    req = requests.get('http://{}/logs/view.cgi?which=100&_HTTP_ID={}'.format(ROUTER_IP, HTTP_ID),
                        auth=requests.auth.HTTPBasicAuth(ROUTER_USERNAME, ROUTER_PASSWORD))
    data = req.text;
    return data

def get_bandwidth(ROUTER_IP, ROUTER_USERNAME, ROUTER_PASSWORD, HTTP_ID):
    req = requests.post('http://{}/update.cgi'.format(ROUTER_IP),
                        data={'exec':'iptraffic','_HTTP_ID':HTTP_ID},
                        auth=requests.auth.HTTPBasicAuth(ROUTER_USERNAME, ROUTER_PASSWORD))
    data = req.text;
    data = format_bandwidth_data(data)
    return data

def format_bandwidth_data(data):
    #format data dynamically
    exec(data)
    #r = redis.StrictRedis(ROUTER_IP=myenv.redisROUTER_IP, port=6379, db=0)
    #ROUTER_IP	Download (bytes/s)	Upload (bytes/s)	TCP IN/OUT (pkt/s)	UDP IN/OUT (pkt/s)	ICMP IN/OUT (pkt/s)	TCP Connections	UDP Connections
    
    header = 'ROUTER_IP,', 'download,', 'upload,', 'total bandwidth';
    #csv format
    #print header
    jsonList=[header]
    for item in iptraffic:
        ROUTER_IP = item[0]
        download = item[1]
        upload = item[2]
        tcp = item[3]
        udp = item[4]
        icmp = item[5]
        tcpconn = item[6]
        udpconn = item[7]

        #setup redis save here
        #r.set('ROUTER_IP', ROUTER_IP)
        
        #csv format
        #print '{}, {}, {}, {}'.format(ROUTER_IP, size(download), size(upload), totalbandwidth)
    
        totalbandwidth = size(download + upload)
        itemList=[ROUTER_IP, size(download), size(upload), totalbandwidth]
        jsonList.append(itemList)   
        
    return json.dumps(jsonList)


#example get device list
#print get_device_list(myenv.ip, myenv.ROUTER_USERNAME, myenv.ROUTER_PASSWORD, myenv.httpid)

#print logs example
#print get_log(myenv.ip, myenv.ROUTER_USERNAME, myenv.ROUTER_PASSWORD, myenv.httpid)

#print bandwidth example as json format
print get_bandwidth(myenv.ip, myenv.ROUTER_USERNAME, myenv.ROUTER_PASSWORD, myenv.httpid)



