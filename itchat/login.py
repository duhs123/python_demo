import itchat

#扫描控制台登录
def scan_console_login():
    itchat.auto_login(enableCmdQR=1,hotReload=True)
    itchat.dump_login_status()
#扫描图片台登录
def confirm_login():
    itchat.auto_login(hotReload=True)
    itchat.dump_login_status()
def confirm_login_with_callback():
    itchat.auto_login(hotReload=True,loginCallback=after_login, exitCallback=after_logout)
    itchat.dump_login_status()
#等入后方法
def after_login():
    print("登录后调用")
#登出后方法
def after_logout():
    print("退出后调用")

if __name__ == '__main__':
    confirm_login_with_callback()
    itchat.send('Hello, 自己群聊', toUserName=itchat.search_chatrooms(name=u'自己群聊')[0]['UserName'])
