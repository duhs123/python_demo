#coding: utf-8
import json
a1="你好！"
a2="我好！"
a=[a1,a2]
print json.dumps(a,ensure_ascii=False)