import json
import webbrowser
from datetime import datetime

with open('./json/result.json', 'r', encoding='utf-8') as r:
    resultDict = json.load(r)
result = resultDict['lqxx']
result = result['ResultBody']

with open('temp.html', 'r', encoding='utf-8') as r:
    string = r.read()
    string = string.replace('replaceName', resultDict['xm'])
    string = string.replace('replacePCMC', result['PCMC'])
    string = string.replace('replaceKLMC', result['KLMC'])
    string = string.replace('replaceCCMC', result['CCMC'])
    string = string.replace('replaceYXDH', result['YXDH'])
    string = string.replace('replaceYXMC', result['YXMC'])
    string = string.replace('replaceZYDH', result['ZYDH'])
    string = string.replace('replaceZYMC', result['ZYMC'])
    string = string.replace('replaceLQSJ', result['LQSJ'])

with open('index.html', 'w', encoding='utf-8') as w:
    w.write(string)

print(datetime.now(), '写入文件成功!')

webbrowser.open_new_tab('index.html')
