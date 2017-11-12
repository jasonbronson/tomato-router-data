#!/usr/bin/python
import re
import json 
import requests
import myenv
 
def get_device_list(host, username, password, http_id):
    req = requests.post('http://{}/update.cgi'.format(host),
                        data={'_http_id':http_id, 'exec':'devlist'},
                        auth=requests.auth.HTTPBasicAuth(username, password))
 
    tomato = {param: json.loads(value.replace("\'",'\"'))
             for param, value in re.findall(r"(?P<param>\w*) = (?P<value>.*);", req.text)
             if param != "dhcpd_static"}
 
    req = requests.get('http://{}/wireless.jsx?_http_id={}'.format(host, http_id),
                        auth=requests.auth.HTTPBasicAuth(username, password))
 
    tomato.update({param: json.loads(value.replace("'",'"'))
                    for param, value in re.findall(r"(?P<param>\w*) = (?P<value>.*);", req.text)
                    if param != 'u'})
 
    return tomato
 
def get_log(host, username, password, http_id):
    req = requests.get('http://{}/view.cgi?which=100&_http_id='.format(http_id),
                        auth=requests.auth.HTTPBasicAuth(username, password))

    data = {param: json.loads(value.replace("\'",'\"'))
             for param, value in re.findall(r"(?P<param>\w*) = (?P<value>.*);", req.text)
             if param != "dhcpd_static"}

    data.update({param: json.loads(value.replace("'",'"'))
                    for param, value in re.findall(r"(?P<param>\w*) = (?P<value>.*);", req.text)
                    if param != 'u'})

    return data

#http://192.168.1.1/logs/view.cgi?which=100&_http_id=TIDd8d12e0247886bc5

#print get_device_list(myenv.ip, myenv.username, myenv.password, myenv.httpid)
print get_log(myenv.ip, myenv.username, myenv.password, myenv.httpid)



