#!/usr/bin/env 


import urllib2
import json
from datetime import datetime

#Parameters :
symbol = 'ETH'
currency = 'EUR'
timestamp = '1479207600'

# 1/11/2016 11h UCT : 1477998000
# 15/11/2016 11h UCT : 1479207600
# 30/11 : 1480503600


liste = []
liste2 = []

# 'https://www.cryptocompare.com/api/data/pricehistorical?fsym=BTC&tsyms=USD&ts=1452470400'
while timestamp != 1480676400: 
	timestamp = str(timestamp)
	url = 'https://www.cryptocompare.com/api/data/pricehistorical?fsym=' + symbol + '&tsyms='+ currency + '&ts=' + timestamp

	json_obj = urllib2.urlopen(url)

	data = json.load(json_obj)

	for item in data['Data']:
		liste.append(item['Price'])

		# print item['Price']
		# print datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')

		liste2.append(datetime.fromtimestamp(int(timestamp))) #.strftime('%Y-%m-%d')) #('%Y-%m-%d %H:%M:%S')
	timestamp = int(timestamp) + 86400
	#print timestamp


print (liste)
print (liste2)



import matplotlib.pyplot as plt
import matplotlib.dates as mdates

x = liste2
# x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(17)]
y = liste


# print x
# print y

# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# splt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
# plt.gcf().autofmt_xdate()


# plt.plot([2016-11-15, 2016-11-16, 2016-11-18],[3,4,8])
plt.gcf().autofmt_xdate()
plt.show()