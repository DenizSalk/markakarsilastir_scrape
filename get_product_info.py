# -*- coding: utf-8 -*-
import json
import time
import requests
from bs4 import BeautifulSoup
files =[""
        ]
for categotyfile in files:
    f = open(categotyfile, "r" , encoding="utf-8")
    print(categotyfile)
    lines = f.read().splitlines()
    data_list = []

    for url in lines:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser', from_encoding='utf-8')
        try:
            name = soup.find('div', attrs={'class': 'products'}).find("h1").get_text()
            namestr = str(name)
        except:
            namestr = "NULL"
            print("kategori okunamadı")
        try:
            barcodestr = soup.find('div', attrs={'class': 'products'}).find("h2").get_text()
            barcodestr = str(barcodestr)
        except:
            barcodestr = "NULL"
            print("kategori okunamadı")
        data = {
            'Name': namestr,
            'BarcodeI': barcodestr
        }
        data_list.append(data)
        newfile = "output2" + categotyfile
        print(url)
        with open(newfile, 'w', encoding="utf-8") as f:
            json.dump(data_list, f, indent=4, ensure_ascii=False)