import json
import base64
import hashlib
from datetime import datetime


def printf(str0):
    print(datetime.now(), str0)
    return


def sha1_enc(str0):
    enc = hashlib.sha1()
    enc.update(str0.encode('utf-8'))
    return enc.hexdigest()


with open('./json/info.json', 'r', encoding='utf-8') as r:
    infoDict = json.load(r)
    printf('读取身份信息成功!')

sum0 = infoDict['ksh'] + infoDict['zkzh'] + infoDict['id']
sumF = '{{"hashid":"{}"}}'.format(sha1_enc(sum0))
sumB = str(base64.urlsafe_b64encode(sumF.encode('utf-8')), 'utf-8')
if sumB.endswith('='):
    sumB = sumB.replace('=', '')
infoDict['infoCode'] = sumB
printf('编码身份信息成功!')

with open('./json/info.json', 'w', encoding='utf-8') as w:
    json.dump(infoDict, w)
    printf('写入编码信息成功!')
