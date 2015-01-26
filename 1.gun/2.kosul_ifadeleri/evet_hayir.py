#!/usr/bin/env python
# -*- coding: utf-8 -*- 
hava_durumu = "Bulutlu"
url = "http://haftalikhavadurumu.net/api.php?city=Eskisehir"
import urllib
import json
hava_durumu_url = urllib.urlopen(url).read()
hava_durumu = json.loads(hava_durumu_url)
print hava_durumu["data"]["skytext"]
if (hava_durumu == "Güneşli"):
	print "Ders için pek uygun bir gün değil"
elif ( hava_durumu == "Bulutlu"):
	print "Ders için güzel bir gün"
else:
	print "Derse neden geldik ki?"

