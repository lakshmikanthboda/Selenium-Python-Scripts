from selenium import webdriver
from bs4 import BeautifulSoup
import time
dr = webdriver.Chrome()
g=dr.get('https://epaper.ntnews.com/')
print('Finding Availabe Data.............')
time.sleep(20)
h=dr.page_source
soup = BeautifulSoup(h,'html.parser')
urls=[]
for a in soup.find_all('a', href=True):
    urls.append('https://epaper.ntnews.com'+a['href'])
print('Found:- ',str(len(urls)))
def go(urls):
    h=0
    for url in urls:
        try:
            h+=1
            downlode(url)
            print('Downloded:-', str(h))
        except:
            downlode(url)
    print('Downlode Completed for '+str(h)+' Files')

def downlode(url):
    dr.get(url)
    time.sleep(5)
    dr.find_element_by_xpath('/html/body/div[12]/ul/li[3]/div/span[3]/i').click()


go(urls)














