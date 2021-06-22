import urllib3

http=urllib3.PoolManager()

url="http://www.baidu.com"

response=http.request('get',url)
print(response.status)
print(response.data.decode('utf8'))
