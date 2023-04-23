import subprocess
import os
from configparser import ConfigParser
print("软件由河南农业大学学生制作,个人网站Aprdec.top")
print("配置文件在D盘")
f = "D:\login.ini"
con = ConfigParser();
if os.path.isfile(f):
    con.read(f,encoding="utf-8")
    username = con.get("login","username")
    password = con.get("login","password")
else:
    username = input("输入校园网账号:")
    password = input("输入校园网密码:")
    con.add_section("login");
    con.set("login","username",username)
    con.set("login","password",password)
    con.write(open(f,'w'));
session_command ="""$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
Invoke-WebRequest -UseBasicParsing -Uri "http://10.0.108.3/a70.htm" `
-Method "POST" `
-WebSession $session `
-Headers @{
"Accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  "Accept-Encoding"="gzip, deflate"
  "Accept-Language"="zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
  "Cache-Control"="max-age=0"
  "Origin"="http://10.0.108.3"
  "Referer"="http://10.0.108.3/a70.htm"
  "Upgrade-Insecure-Requests"="1"
} `
-ContentType "application/x-www-form-urlencoded" `
-Body "DDDDD="""
session_command +=username
session_command +='&upass='
session_command +=password
session_command +='&R1=0&R2=&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login=&v6ip=";'
# 使用subprocess模块执行PowerShell命令
subprocess.run(['powershell', '-Command', session_command])
