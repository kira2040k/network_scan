import requests,os
File_write = open('funs.py','w')
File_write2 = open('scan.py','w')
File_write3 = open('update.py','w')
funs = requests.get('https://raw.githubusercontent.com/kira2040k/network_scan/main/funs.py').text
scan = requests.get('https://raw.githubusercontent.com/kira2040k/network_scan/main/scan.py').text
update = requests.get('https://raw.githubusercontent.com/kira2040k/network_scan/main/update.py').text
File_write.write(funs)
File_write2.write(scan)
File_write3.write(update)
