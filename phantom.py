import os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
os.chdir('g:\pythonwork\ImdbpostersScapedd')

driver = webdriver.PhantomJS(executable_path=r'C:\Users\Anany\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
k=1
def scrap(url): 
	global k 
	driver.get(url)
	soup=BeautifulSoup(driver.page_source,'lxml')
	x=soup.find(class_='media_index_thumb_list')
	y=x.find_all('a')
	z=[]
	for i in y:
		z.append('https://www.imdb.com'+(i['href']))
	dr = webdriver.PhantomJS(executable_path=r'C:\Users\Anany\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	for i in z:
		dr.get(i)
		soup=BeautifulSoup(dr.page_source,'lxml')
		a=soup.find_all(class_='pswp__zoom-wrap')
		b=a[1].find_all(class_='pswp__img')
		l=(b[1]['alt'])
		with open('%d%s.jpg'%(k,l),'wb')as pic:
			print(b[1])
			k+=1
			pic.write(requests.get(b[1]['src']).content)
driver = webdriver.PhantomJS(executable_path=r'C:\Users\Anany\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
for i in range (1,49):
	url='https://www.imdb.com/gallery/rg1624939264?page=%d&ref_=rgmi_mi_sm'%(i)
	scrap(url)
driver.close()


