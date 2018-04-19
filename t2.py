import itchat
@itchat.msg_register(itchat.content.TEXT)
def _(msg):
    # equals to print(msg['FromUserName'])
    print(msg.fromUserName)
itchat.auto_login()
itchat.auto_login(hotReload=True, enableCmdQR=True, )
author = itchat.search_friends(nickName='Amis')[0]
author = itchat.search_friends(nickName='天柱山')[0]
author.send('greeting, 女王大人!')
itchat.logout()
# itchat.send('Hello, 李碧雯', toUserName='李碧雯')