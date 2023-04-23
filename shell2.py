import subprocess
username = input("输入校园网账号:")
password = input("输入校园网密码:")
session_command = 'New-Object Microsoft.PowerShell.Commands.WebRequestSession;'
session_command += '$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48";'
session_command += 'Invoke-WebRequest -UseBasicParsing -Uri "http://10.0.108.3/a70.htm" '
session_command += '-Method "POST" '
session_command += '-WebSession $session '
session_command += '-Headers @{'
session_command += '"Accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7";'
session_command += '"Accept-Encoding"="gzip, deflate";'
session_command += '"Accept-Language"="zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6";'
session_command += '"Cache-Control"="max-age=0";'
session_command += '"Origin"="http://10.0.108.3";'
session_command += '"Referer"="http://10.0.108.3/a70.htm";'
session_command += '"Upgrade-Insecure-Requests"="1";'
session_command += '} '
session_command += '-ContentType "application/x-www-form-urlencoded" '
"""
session_command += '-Body "DDDDD=2110122076&upass=12345678&R1=0&R2=&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login=&v6ip=";'
"""
session_command +='-Body "DDDDD='
session_command +=username
session_command +='&upass='
session_command +=password
session_command +='&R1=0&R2=&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login=&v6ip=";'
# 使用subprocess模块执行PowerShell命令
subprocess.run(['powershell', '-Command', session_command])
