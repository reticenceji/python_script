import re
import requests

url = "http://doc.xqxt.com/%E5%88%9D%E4%B8%AD%E6%95%B0%E5%AD%A6%EF%BC%8C%E7%9F%A5%E8%AF%86%E8%AE%B2%E8%A7%A3+%E5%B7%A9%E5%9B%BA%E7%BB%83%E4%B9%A0%EF%BC%8C%E5%88%9D%E4%B8%80%E8%87%B3%E5%88%9D%E4%B8%89%E4%B8%8A%E4%B8%8B%E5%86%8C%EF%BC%8C%E5%9F%BA%E7%A1%80%E7%89%88%E5%92%8C%E6%8F%90%E9%AB%98%E7%89%88%E9%85%8D%E8%AF%A6%E7%BB%86%E8%A7%A3%E6%9E%90/01%E5%88%9D%E4%BA%8C%E4%B8%8A%E5%86%8C/"
#构造请求头,伪装浏览器
headers = {
	"user-agent" : "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
dir = "/home/reticence/jiajiao/"
#使用GET方法获得一个response对象,text包含了返回内容
html = requests.get(url,headers=headers).text
#正则表达式,匹配字符串
pattern = r'''<tr><td><a href="(?P<url>.+?)" title="(?P<title>.+?).doc">.+?</a></td>'''
#找出所有的匹配项
herf = re.findall(pattern,html)
for i in herf:
	#使用GET方法获得一个response对象
	doc = requests.get(url+i[0])
	#打开文件
	with open(dir+i[1]+".doc","w+b") as fileobj:
		#content属性是内容的二进制格式
		fileobj.write(doc.content)
	