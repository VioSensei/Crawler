#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import mechanize,sys,re
import requests
from colorama import Fore, Back, Style, init
init(autoreset=True)
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('user-agent',
				  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]

def bilgi():
	print(Fore.RED+"[-] Ornek Kullanım:")
	print(Fore.RED+"[+] python crawler.py www.google.com")

try:
	dosya = open("sonuc.txt","w")
	link = sys.argv[1]
	denetle = link.split(".")

	if re.findall(":",denetle[0]):
		bilgi()
		sys.exit()

	d_link = "http://"+link
	print("Start scanning...  >>  "+link)

	br.open(d_link)
	for links in br.links():
		if re.findall(denetle[1],links.url):
			dosya.write(links.url+"\n")
		else:
			dosya.write(d_link+links.url+"\n")
	print("Bitti sonuçlar dosyaya kaydedildi. >> sonuc.txt")

except:
	bilgi()