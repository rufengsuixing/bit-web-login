$username=""
$password=""
function utf16_utf8 ($x) 
{ 
$data = [System.Text.Encoding]::GetEncoding('utf-16').GetBytes($x)
    $res=@() 
    foreach ($n in $data)
    { 
    if ($n -ne 0)
        {$res+=$n
        }
    }
$data = [System.Text.Encoding]::GetEncoding('utf-8').GetString($res)
return $data
}
$bodyl = @{
    "action"="login"
    "username"=$username
    "password"=$password
    "ac_id"="1"
    "user_ip"=""
    "nas_ip"=""
    "user_mac"=""
    "save_me"="0"
    "ajax"="1"
}
$bodyo = @{
    "action"="logout"
    "username"=$username
    "password"=$password
    "ac_id"="1"
    "user_ip"=""
    "nas_ip"=""
    "user_mac"=""
    "save_me"="0"
    "ajax"="1"
}
$ie2 =Invoke-WebRequest http://www.baidu.com -Method GET -MaximumRedirection 0
while ($ie2.StatusCode -ne 200)
    {
    if ($fan.Contains("online"))
        {
        $ie =Invoke-WebRequest http://10.0.0.55:802/include/auth_action.php -Method POST -Body $bodyo
        $fan=utf16_utf8 ($ie.Content) 
        $fan
        sleep 1
        }
    $ie =Invoke-WebRequest http://10.0.0.55:802/include/auth_action.php -Method POST -Body $bodyl
    $fan=utf16_utf8 ($ie.Content) 
    $fan
    if ($fan.Contains("请填写"))
    {echo "你没填全"
        break
    }
    sleep 1
    $ie2 =Invoke-WebRequest http://www.baidu.com -Method GET -MaximumRedirection 0
    }
    '程序已停止'
    $null = [System.Console]::ReadKey()
