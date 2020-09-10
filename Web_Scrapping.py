import requests
from bs4 import BeautifulSoup
import re
dagta=[]
p=requests.get('https://www.bestmobile.pk/used-mobiles')
soup=BeautifulSoup(p.content,'html.parser')
b=soup.findAll("div",{"class":"media-left"})
bw=soup.findAll("div",{"class":"media-body"})
a=soup.findAll("div",{"class":"ribbon"})
for i in range(0,len(a)):
    r=a[i].text
    r=r.split(' ')
    print(r[1].strip())
##for i in range(0,len(a)):
    ##print(a[i].text.strip())
    

