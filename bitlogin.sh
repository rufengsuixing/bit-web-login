#for router
if ! ping -c 3 www.baidu.com  ; then
    username=
    password=
    post_data='action=login&username='$username'&password='$password'&ac_id=1&&user_ip=&nas_ip=&user_mac=&save_me=1&ajax=1'
    url="http://10.0.0.55:801/include/auth_action.php"
    returnstr=`curl -d $post_data $url`
    logger -t "【自动登陆】" "用户$username登陆,状态$returnstr"
fi
