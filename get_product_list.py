import time
import os
import requests
from bs4 import BeautifulSoup
maincat = [""
]
for cats in maincat:
	for x in range(1,100):
		url = cats
		urlend = '/?sayfa='
		urlfinal = url + urlend + str(x)
		reqs = requests.get(urlfinal)
		soup = BeautifulSoup(reqs.text, 'html.parser')
		for link in soup.find_all('a', attrs={'class' : 'add-to-cart'}):
			try:
				catname = str(url.replace("https://marketkarsilastir.com/", "") + ".txt")
				catnamev2 = catname.replace("/", "-")
				print("https://marketkarsilastir.com/" + link['href'])
				charmapfix = link['href'].replace("\x92","0")
				with open(catnamev2, 'a') as f:
					f.write("https://marketkarsilastir.com" + link['href'] + "\n" )
					f.close()
			except:
				break
		print("sayfa:" + str(x))
	else:
	  print("Finally finished!")