import datetime
import requests
from bs4 import BeautifulSoup
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

url="http://menu.yalova.edu.tr/"
r = requests.get(url)

soup=BeautifulSoup(r.content,"html.parser")

gelen_veri =soup.find_all("ul", {"class": "home-table"})
csvFile=open('test.csv','w+')

for y in gelen_veri:
    yemek_bas=y.find_all("li",{"data-toggle":"tooltip"})
    src=y.find_all("li")

    writer = csv.writer(csvFile)
    writer.writerow(('', 'Yemek listesi'))
    for i in range(0,120,6):
        liste = src[i].text.replace("\r", "").replace("\n", "")
        writer.writerow((liste[0:25],liste))
    csvFile.close()




