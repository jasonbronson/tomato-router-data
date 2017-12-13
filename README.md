# Tomato Router Stats using python


Reads tomato router data for graphing or logging


Feature list:

 * get logs
 * get bandwidth by device host
 * get device list
 * get websearch history


Enjoy :+1:


# installation
Some items are optional to install (example redis)
```sudo pip install -U python-dotenv
sudo pip install requests
sudo pip install dotenv
pip install -U python-dotenv
sudo pip install requests
sudo pip install redis
sudo pip install hurry.filesize
```

Setup your own .env file 

Edit the envsample file and run this command
```
cp envsample > .env
```


#example output

```
["host,", "download,", "upload,", "total bandwidth"], ["192.168.1.2", "2M", "27K", "2M"], ["192.168.1.3", "608B", "608B", "1K"], ["192.168.1.4", "608B", "608B", "1K"], ["192.168.1.9", "2M", "836K", "3M"], ["192.168.
1.11", "259K", "137K", "396K"], ["192.168.1.30", "34K", "13K", "48K"], ["192.168.1.100", "7K", "31K", "39K"], ["192.168.1.120", "720B", "0B", "720B"], ["192.168.1.132", "546M", "12M", "559M"], ["192.168.1.133", "422M
", "13M", "435M"], ["192.168.1.134", "232M", "4M", "237M"], ["192.168.1.138", "3M", "369K", "4M"], ["192.168.1.139", "549K", "3M", "3M"], ["192.168.1.140", "413M", "71M", "484M"], ["192.168.1.141", "9K", "22K", "32K"
], ["192.168.1.142", "289M", "11M", "300M"], ["192.168.1.143", "548M", "10M", "558M"], ["192.168.1.144", "1G", "17M", "1G"], ["192.168.1.145", "570K", "2M", "2M"], ["192.168.1.147", "5M", "444K", "6M"], ["192.168.1.1
48", "1G", "33M", "1G"], ["192.168.1.149", "831M", "108M", "939M"], ["192.168.1.150", "10M", "1M", "11M"], ["192.168.1.157", "194M", "10M", "204M"], ["192.168.1.160", "0B", "40B", "40B"], ["192.168.1.177", "129M", "1
1M", "140M"], ["192.168.1.202", "257K", "19K", "276K"], ["192.168.1.205", "305M", "22M", "328M"], ["192.168.1.206", "5M", "3M", "8M"], ["192.168.1.212", "85M", "7M", "92M"], ["192.168.1.218", "196K", "275K", "471K"]
```

Inspired by
[tomato api documentation](http://paulusschoutsen.nl/blog/2013/10/tomato-api-documentation/)

Tomato firmware
[tomato router firmware](http://tomato.groov.pl/)

