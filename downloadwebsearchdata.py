import csv,re,requests,sys,MyEnv
import MySQLdb as my
#pip install mysqlclient

url = 'http://' + MyEnv.ROUTER_IP + '/webmon_recent_domains?_http_id=' + sys.argv[1]

response = requests.get(url,
                        auth=requests.auth.HTTPBasicAuth(
                          MyEnv.ROUTER_USERNAME,
                          MyEnv.ROUTER_PASSWORD))
#print response.text

db = my.connect(host=MyEnv.MYSQL_IP,
user=MyEnv.MYSQL_USERNAME,
passwd=MyEnv.MYSQL_PASSWORD,
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