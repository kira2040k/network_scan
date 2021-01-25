import subprocess,re,socket,json,requests,argparse,time
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

    API = 'at_RPjMc0F8janKTVeWjnxIf2bks2LD4'
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

def programs():
    print('please wait....')
    output = subprocess.check_output("netstat -nb", shell=True)
    time.sleep(8)
    output = output.decode("utf-8")
    PID = re.findall('.*exe',output)
    
    output2 = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}|.*exe',output)
    
    for ips in output2:
        #print(ips) 
        ip = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}',ips)
        service = re.findall('.*exe',ips)
        try:
            if('.exe' in service[0]):
                service = str(service[0]).replace('[','')
                print('Program:',service)
        except:
            pass               

        try:
            if(re.search('443$',ips)):
                print('\033[1;32;40m',ip[0])
            else:
                print('\033[1;31;40m',ip[0])
                
        except:
            pass

