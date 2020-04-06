from selenium import webdriver
from bs4 import BeautifulSoup
import xlwt
dr=webdriver.Chrome()
for i in range(0,10):
  dr.get('https://www.pagalworld.mobi/home/updates?page='+str(i))
  g=dr.page_source
  soup=BeautifulSoup(g,'html.parser')
  #f=soup.find_all('ul')
  urls = []
  for a in soup.find_all('a', href=True):
    urls.append(a['href'])
  songs=[]
  for u in range(1,61,3):
    songs.append(urls[u])
  break
import time

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
i=1
for s in songs:

  #dr = webdriver.Chrome()
  dr.get(s)
  time.sleep(4)
  soupp = BeautifulSoup(dr.page_source,'html.parser')
  n=soupp.find('div',class_='col-xs-12 col-sm-12 col-md-12 col-lg-12 padding-10px')
  n=n.text
  name=n.strip()
  ws.write(i, 0, name)
  print(n.strip())
  pp=soupp.find_all('div',class_='col-xs-8 col-sm-12 col-md-9 col-lg-9 f-desc')
  print(pp[1].text)
  ws.write(i, 1, pp[1].text)
  g=(soupp.find('div',class_='alb-img-det'))
  print('https://www.pagalworld.mobi'+str(g.img['src']))
  ws.write(i,2,'https://www.pagalworld.mobi'+str(g.img['src']))
  dr.find_element_by_class_name('dbutton').click()
  # Cloudinary settings using python code. Run before pycloudinary is used.
  time.sleep(60)
  import cloudinary

  cloudinary.config(
    cloud_name='cloud name',
    api_key='key',
    api_secret='api'
  )
  import cloudinary.uploader
  import cloudinary.api

  url = "C:/Users/dell/Downloads/"
  file = name + '.mp3'
  url = url + file
  f = cloudinary.uploader.upload(url,
                                 resource_type="video")
  ws.write(i,3,f['url'])
  print(f['url'])
  wb.save('example.xls')
  i+=1
