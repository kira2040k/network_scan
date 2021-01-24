import subprocess,re,socket,json,requests,argparse
def fast():
    output = subprocess.check_output("netstat -n", shell=True)
    output = output.decode("utf-8")
    output2 = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}',output)
    for ips in output2:
        check = re.search('^127.0.0.1|^74.125.34.46|^192.168.',ips)
        if(check):
            pass
        else:
            
            ip = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',ips)
            ip = ip[0]
            if(re.search('443$',ips)):
                print('\033[1;32;40m',ips)
            else:
                    print('\033[1;31;40m',ips)
            
def full():
    API = 'your API here'
    output = subprocess.check_output("netstat -n", shell=True)
    output = output.decode("utf-8")
    output2 = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}',output)
    for ips in output2:
        check = re.search('^127.0.0.1|^74.125.34.46|^192.168.',ips)
        if(check):
            pass
        else:
            
            ip = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',ips)
            ip = ip[0]
            if(re.search('443$',ips)):
                print('\033[1;32;40m',ips,end='')
            else:
                    print('\033[1;31;40m',ips,end='')
            
            try:
                r =  requests.get('https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={}&ipAddress={}'.format(API,ip))
                r = json.loads(r.text)

                print(' ','Country:',r['location']['country'],end='')
                print(' ','ISP:',r['isp'])
                
                
            except:
                print('\n' +ips)
                pass
