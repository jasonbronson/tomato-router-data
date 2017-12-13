import re,requests,sys,myenv
import MySQLdb as my
#pip install mysqlclient

url = 'http://' + myenv.ROUTER_IP + '/webmon_recent_domains?_http_id=' + myenv.HTTP_ID

response = requests.get(url,
                        auth=requests.auth.HTTPBasicAuth(
                          myenv.ROUTER_USERNAME,
                          myenv.ROUTER_PASSWORD))
#print response.text

db = my.connect(host=myenv.MYSQL_IP,
user=myenv.MYSQL_USERNAME,
passwd=myenv.MYSQL_PASSWORD,
db="router"
)

cursor = db.cursor()

import StringIO
s = StringIO.StringIO(response.text)
for line in s:
    data = re.split(r'\t+', line.replace("\n", ""))
    id = data[0]
    ip = data[1]
    domain = data[2]
    sql = "INSERT IGNORE INTO `websearch` (`timestamp`, `ip`, `domain`) VALUES ('%s', '%s', '%s')" % \
    (id, ip, domain)
    number_of_rows = cursor.execute(sql)
    db.commit()

db.close()