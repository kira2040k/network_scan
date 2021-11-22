import subprocess,re,socket,json,requests,argparse,time,random,virus_total_apis,os,colors
def fast():
    print('scan running....')
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
                print(ips)
            else:
                    print(ips)
            
def full():
    print('scan running....')
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
                print(ips,end='')
            else:
                    print(ips,end='')
            
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
    output = output.decode("utf-8")    
    output2 = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}|.*exe',output)
    
    for ips in output2:
        
        ip = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}',ips)
        service = re.findall('.*exe',ips)
        try:
            if('.exe' in service[0]):
                service = str(service[0]).replace('[','')
                print('Program:',service)
                print("-"*15)
        except:
            pass               

        try:
            print(ip[0])
           
                
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
                print(new)
                print(hash1[0])
                check.append(str(Progrmas_paths[0]))
                response  = API.get_file_report(hash1[0])
                response = json.dumps(response)
                response = json.loads(response)
                print(f"{response['results']['positives']}/70")
                time.sleep(26)
                
        except:
            pass        

def banner():
    file = open('banner.txt',encoding='utf-8')
    
    print(file.read())

def files():

    
    
    path = input('Enter Path:')
    API = '35a7358ed8946a8b0cd66024d16f36881e14ce38328c03ec3c03f5bf45f97d67'
    API = virus_total_apis.PublicApi(API)
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
            
    for f in files:

        print(f' {f}')
        
        output = subprocess.check_output(f"certutil -hashfile \"{f}\" MD5")
        output = output.decode("utf-8")
        hash1 = re.findall('[a-z|A-Z|0-9]{32}',output)
        try:
            response  = API.get_file_report(hash1[0])
            response  = API.get_file_report(hash1[0])
            response = json.dumps(response)
            response = json.loads(response)
            
            time.sleep(26)
            print(f"{response['results']['positives']}/56")
        except:
            print('clean file')
            pass

def Scanhide():
    path  = input('Path to scan:')
    try:
        output = subprocess.check_output(f"dir /r {path}", shell=True)
        output = output.decode("utf-8",errors='ignore')
    except:
        pass
    find = re.findall('[0-9]{1,100}.*\$DATA',output)
    for find in find:
        try:
            file_hide = re.findall(':.*:',find)
            original_file = re.findall('[0-9]{1,100} .*:\$',find)
            original_file = re.findall('\s[a-z,A-Z,0-9]{1,100}\.[a-z,A-Z,0-9]{1,100}',original_file[0])
            file_hide = re.findall('[a-z,A-Z,0-9]{1,100}\.[a-z,A-Z,0-9]{1,100}',file_hide[0])
            output = subprocess.check_output(f"more< {original_file[0]}:{file_hide[0]} > {file_hide[0]}", shell=True)
            print(f'find {file_hide[0]} on {original_file[0]}  and extracted successfully ')
        except:
            exit('not Found hideen files')

def hide():
    file_hide = input('any file: ')
    file_hidden = input('file you want to hide: ')
    try:
        output = subprocess.check_output(f"type {file_hidden} > {file_hide}:{file_hidden}", shell=True)
    except:
        print('error check your input..')

