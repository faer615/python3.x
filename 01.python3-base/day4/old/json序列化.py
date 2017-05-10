#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
# json序列化
import json

info = {
    'name':'felix',
    'age':22
}

f = open("test.text","w")
f.write(json.dumps(info))

f.close()

#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
# json反序列化
import json

f = open("test.text","r")

data = json.loads(f.read())

print(data["age"])
