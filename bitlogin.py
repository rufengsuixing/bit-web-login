import sys,queue,os
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
mishi='example1nfi79snf'
class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0')
def jiami():
    pc = prpcrypt(mishi)
    print("-------生成密码程序----------")
    username = input("请输入用户名：")
    u = pc.encrypt(username)
    password = input("请输入密码：")
    p = pc.encrypt(password)
    r=os.popen('wmic csproduct get UUID')
    info=r.readlines()
    b = pc.encrypt(username+info[2].strip()+password)
    f = open('naprd','wb')
    f.write(u+b'\n'+p+b'\n'+b)
    f.close()
    print('已生成本机唯一密匙，文件被拿走也没用')
def link(username,password):
    import requests
    url = 'http://10.0.0.55:802/include/auth_action.php'
    headers={
    'Host': '10.0.0.55:802',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://10.0.0.55:802/srun_portal_pc.php?ac_id=1&',
    'Connection': 'keep-alive'
    }
    payload = {'action':'login','username':username,'password':password,'ac_id':'1','user_ip':'','nas_ip':'','user_mac':'','save_me':'0','ajax':'1'}
    r = requests.post(url, headers=headers,data=payload)
    r.encoding="UTF-8"
    return r.text
def jiemi():
    pc = prpcrypt(mishi)
    try:
        f = open('naprd','rb')
        u=f.readline()
        p=f.readline()
        b=f.readline()
        f.close()
    except:
        raise
    username=pc.decrypt(u.strip()).decode()
    password=pc.decrypt(p.strip()).decode()
    r=os.popen('wmic csproduct get UUID')
    info=r.readlines()
    bn = pc.encrypt(username+info[2].strip()+password)
    if bn==b.strip():
        return [username,password]
    else:
        raise ValueError("invavid id")
def down(username,passwd):
    import requests
    url = 'http://10.0.0.55:802/include/auth_action.php'
    headers={
    'Host': '10.0.0.55:802',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://10.0.0.55:802/srun_portal_pc.php?ac_id=1&',
    'Connection': 'keep-alive'
    }
    payload = {'action':'logout','username':username,'password':passwd,'ac_id':'1','ajax':'1'}
    r = requests.post(url, headers=headers,data=payload)
    r.encoding="UTF-8"
    return r.text
def main(argv=''):
    if len(argv)==2:
        if argv[1]=='jiami':
            jiami()
            exit()
    try:
        [username,password]=jiemi()
    except IOError:
        print('读写错误，是否生成密码文件')
        jiami()
        input("按任意键登陆")
        main()
        exit()
    except ValueError:
        print('新机器请重新生成密码')
        jiami()
        input("按任意键登陆")
        main()
        exit()
    except:
        print('未知错误')
        exit()
    if len(argv)==2:
        if argv[1]=='logout':
            text=down(username,password)
            print(text)
            input("按任意键关闭")
            exit()
    text=link(username,password)
    print(text)
    input("按任意键关闭")
    exit()
        
if __name__ == '__main__':
    main(sys.argv)