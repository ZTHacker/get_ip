#coding=utf-8
#by www.zhangteng.xyz
#2019.5.11
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


head={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
#发送get请求并得到结果

url = 'http://ip.tool.chinaz.com/'
	
req= requests.get(url,headers=head)  #发送请求

req.encoding = 'utf-8'


soup = BeautifulSoup(req.text,'html.parser')

html = soup.prettify()

div = soup.find_all('div',attrs={'class','IpMainWrap-right fr'})

print(div[0].encode('utf-8'))
