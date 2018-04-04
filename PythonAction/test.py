import requests
url = 'http://www.baidu.com'
data = requests.get(url)
print(data.text)
