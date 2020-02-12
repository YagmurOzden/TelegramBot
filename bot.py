import datetime
import requests
from bs4 import BeautifulSoup


url="http://menu.yalova.edu.tr/"

r = requests.get(url)

soup=BeautifulSoup(r.content,"html.parser")

gelen_veri =soup.find_all("ul", {"class": "home-table"})
for y in gelen_veri:
    yemek_bas=y.find_all("li",{"data-toggle":"tooltip"})
    src=y.find_all("li")

    src=src[0].text
    src = src.replace("\r", "")
    src = src.replace("\n", "")
    print (src)

    tarih=src[0:30]

    date = datetime.date.today()

    date1 = datetime.datetime.strptime("2020-02-08", "%Y-%m-%d").strftime("%d %m %Y")
