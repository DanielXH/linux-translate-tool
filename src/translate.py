import sys
import urllib.request
import urllib.parse
import json
import random
import hashlib
import argparse

# -----------------------------
# @author: xudongh
# @email: 794243810@qq.com
# -----------------------------


# --------- api 信息 -----------
# 有道翻译
youdaoApi = 'http://openapi.youdao.com/api'
youdaoAppKey = ''
youdaoSecretKey = ''

# -----------------------------

# 查询函数  t: translate
# 有道翻译api
def tYoudao(q): 
  appKey = youdaoAppKey
  secretKey = youdaoSecretKey
  salt = str(random.random())
  signOrigin = (appKey + q + salt + secretKey).encode(encoding='UTF-8')
  sign = hashlib.md5(signOrigin).hexdigest()
  params = {
    'q': q,
    'from': 'auto',
    'to': 'auto',
    'appKey': appKey,
    'salt': salt,
    'sign': sign
  }
  data = bytes(urllib.parse.urlencode(params), encoding='utf8') 
  response = urllib.request.urlopen(youdaoApi, data=data)

  # 查询结果处理
  resultJson = json.loads(response.read())
  if ('errorCode' in resultJson) and resultJson['errorCode'] == '0':
    if 'basic' in resultJson and 'phonetic' in resultJson['basic']:
      print('音标：')
      print('    ' + resultJson['basic']['phonetic'])

    print('翻译:')
    for v in resultJson['translation']:
      print('    ' + v)
    
    if 'basic' in resultJson and 'explains' in resultJson['basic']:
      print('词典：')
      for v in resultJson['basic']['explains']:
        print('    ' + v)
    if 'web' in resultJson:
      print('网络释义：')
      for d in resultJson['web']:
        print('    ' + d['key'] + '：[' + '，'.join(d['value']) + ']')
  else:
    print('没有相关翻译...')

  # print(resultJson)

# main function
def main(words):
  print('查询：')
  print('    ' + words)
  tYoudao(words)

# 
if __name__ == '__main__':
  # 命令参数解释器
  descStr = '一个命令行翻译小工具'
  helpStr = '需要联网使用，目前调用的是有道翻译的api接口；\n' \
          + '支持中文、日文、英文、韩文、法文、俄文、葡萄牙文、西班牙文八种语言\n\n' \

  
  parser = argparse.ArgumentParser(description=descStr, formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument('words', action='store', help=helpStr)
  args = parser.parse_args()
  
  # main()
  main(args.words)
  exit(0)