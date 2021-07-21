import os
import json
import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def printf(str0, str1):
    print(datetime.now(), str0 + str1)
    return


def getScore(str0):
    resultDict = json.loads(requests.get(str0).text)['C']
    name = resultDict['xm']
    result = resultDict['lqxx']

    if 'ResultCode' not in result:
        printf(name, '暂无录取结果!')
    elif result['ResultCode'] == '000':
        printf(name, '有录取结果!')
        printf('', '写入文件中……')
        with open('./json/result.json', 'w', encoding='utf-8') as f:
            json.dump(resultDict, f)
        os.system("python write.py")
        scheduler.pause()
    else:
        printf('', '错误!')
        scheduler.pause()
    return


printf('', '读取编码信息中……')
with open('./json/info.json', 'r', encoding='utf-8') as r:
    infoDict = json.load(r)
if 'infoCode' not in infoDict:
    printf('无编码信息!', '尝试生成中……')
    os.system("python trans.py")
elif infoDict.get('infoCode', True) == '':
    printf('无编码信息!', '尝试生成中……')
    os.system("python trans.py")

with open('./json/info.json', 'r', encoding='utf-8') as r:
    url = 'https://bigapp.scedu.net/gkapi/api/score/' + json.load(r)['infoCode']
    printf('', '读取编码信息成功!')

scheduler = BlockingScheduler()
scheduler.add_job(getScore, 'interval', seconds=int(infoDict['interval']), args=[url])
printf('', '开始请求录取信息!')
printf('时间间隔', infoDict['interval'] + 's')
try:
    getScore(url)
    scheduler.start()
except:
    pass
else:
    pass
