# Tomato Router Stats using python


Reads tomato router data for graphing or logging

Feature list:

 * get logs
 * get bandwidth by device host
 * get device list


Enjoy :+1:


# installation
Some items are optional to install (example redis)
```sudo pip install -U python-dotenv
sudo pip install requests
sudo pip install dotenv
sudo pip install load_dotenv
sudo pip install requests
sudo pip install redis
sudo pip install hurry.filesize
```

Setup your own .env file 

run this in the directory after you download/clone from github then edit it with your details
```
echo "
username=admin
password=admin
httpid=MY-HTTP-ID-GOES-HERE
ip=192.168.1.1
redishost=192.168.1.30
" > .env
```

Inspired by
[tomato api documentation](http://paulusschoutsen.nl/blog/2013/10/tomato-api-documentation/)

Tomato firmware
[tomato router firmware](http://tomato.groov.pl/)

