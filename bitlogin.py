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

if __name__ == '__main__':
    link(sys.argv)