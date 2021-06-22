import urllib3
import json

http = urllib3.PoolManager()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)',
    'Host':'httpbin.org'}
data = {'word':'hello'}
data = json.dumps(data).encode()  # json.dumps方法可以将python对象转换为json对象
response = http.request('POST','http://httpbin.org/post',body=data, headers=headers)
print(response.status,response.data.decode('utf-8'))