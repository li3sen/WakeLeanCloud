import requests
import sys
import time
import leancloud

class Comment(leancloud.Object):
    pass

if (len(sys.argv) >= 3):
    appid = sys.argv[1]
    appsec = sys.argv[2]

leancloud.init(appid, appsec)
comment=Comment()
comment.set('comment','wakeup')
comment.save()
print("唤醒完毕")
