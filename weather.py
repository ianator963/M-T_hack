import requests
from bs4 import BeautifulSoup
import time

file = requests.get("https://weather.com/en-IN/weather/tenday/l/dc3606bad8fa1360d11e515d0e06312e1a9ccd318c216935521c7cce6c362cdf")

soup = BeautifulSoup(file.content, "html.parser")

#content = soup.find(class_ = "card Card--card--2AzRg DailyForecast--Card--1WBkh")
list= []
for word in soup.find_all('p'):
	content=word.get_text()

	list.append(content)

f = f'Day 1: Day: {list[0]} Day 1: Night: {list[1]}\nDay 2: Day: {list[2]} Day 2: Night: {list[3]}\nDay 3: Day: {list[4]} Day 3: Night: {list[5]}\nDay 4: Day: {list[6]} Day 4: Night: {list[7]}\nDay 5: Day: {list[8]} Day 5: Night: {list[9]}\nDay 6: Day: {list[10]} Day 6: Night: {list[11]}\nDay 7: Day: {list[12]} Day 7: Night: {list[13]}\nDay 8: Day: {list[14]} Day 8: Night: {list[15]}'

year, mon, mday, hour, min, sec, wday, yday, isdst = time.localtime()


days = []

new_count = 0
new_mon = 0
for i in range(15):
	day = []
	count = 0
	if new_mon == 0:
		if mon == 1 and mday + i > 31 or mon == 2 and mday + i > 28 or mon == 3 and mday + i > 31 or mon == 4 and mday + i > 30 or mon == 5 and mday + i > 31 or mon == 6 and mday + i > 30 or mon == 7 and mday + i > 31 or mon == 8 and mday + i > 31 or mon == 9 and mday + i > 30 or mon == 10 and mday + i > 31 or mon == 11 and mday + i> 30 or mon == 12 and mday + i > 31:
			count += 1
			mon += 1
			mday = count
			day.append(mon)
			day.append(mday)
			new_mon += 1
		else:
			count += 1
			day.append(mon)
			day.append(mday + i)
		new_count += 1
		days.append(day)
recent = days[-1]
new_mon = recent[0]
for x in range(15 - len(days)):
	new_day = []
	new_day.append(new_mon)
	new_day.append(x + 2)
	days.append(new_day)

print(days)