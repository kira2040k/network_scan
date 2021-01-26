import subprocess,re,socket,json,requests,argparse,time,random,virus_total_apis,os
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

    API = 'your ip-geolocation.whoisxmlapi.com api'
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
    print('scan running....')
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

def ps():
    print('scan running....')
    API = 'your virus total api'
    API = virus_total_apis.PublicApi(API)
    
    os.system("powershell.exe \"get-process | get-item -erroraction silentlycontinue | format-table name, directory\" > proc.txt")
    time.sleep(2)
    file  = open('proc.txt','r')
    Programs = file.read()
    scan = re.findall('.*',Programs)
    check = []
    for pro in scan:
        Programs_name  = re.findall('.*exe',pro)
        
        Progrmas_paths = re.findall('[A-Z]:.*',pro)
        
        try:
            if('\\' in Progrmas_paths[0] and '.exe' in Programs_name[0] and Progrmas_paths[0] not in check):
                new = re.sub(' +', ' ',Progrmas_paths[0])
                new = new.rstrip()+'\\'+Programs_name[0]
                output = subprocess.check_output(f"certutil -hashfile \"{new}\" MD5")
                output = output.decode("utf-8")
                
                hash1 = re.findall('[a-z|A-Z|0-9]{32}',output)
                print('\033[1;32;40m',new)
                print(hash1[0])
                check.append(str(Progrmas_paths[0]))
                response  = API.get_file_report(hash1[0])
                response = json.dumps(response)
                response = json.loads(response)
                print(f"{response['results']['positives']}/70")
                time.sleep(26)
                
        except:
            pass        

