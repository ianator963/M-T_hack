import requests
from bs4 import BeautifulSoup
import time

file = requests.get("https://weather.com/en-IN/weather/tenday/l/dc3606bad8fa1360d11e515d0e06312e1a9ccd318c216935521c7cce6c362cdf")

soup = BeautifulSoup(file.content, "html.parser")

list= []
for word in soup.find_all('p'):
	content=word.get_text()

	list.append(content)

year, mon, mday, hour, min, sec, wday, yday, isdst = time.localtime()

days = []

new_count = 0
new_mon = 0
for i in range(15):
	day = []
	count = 0
	if new_mon == 0:
		if (mon == 1 and mday + i > 31 or mon == 2 and mday + i > 28 or mon == 3 and mday + i > 31 or mon == 4 and mday + i > 30 or mon == 5 and mday + i > 31
		or mon == 6 and mday + i > 30 or mon == 7 and mday + i > 31 or mon == 8 and mday + i > 31 or mon == 9 and mday + i > 30 or mon == 10 and mday + i > 31
		or mon == 11 and mday + i> 30 or mon == 12 and mday + i > 31):
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

day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15 = days
g = (f'{day1} Day: {list[0]}\n\tNight: {list[1]}\n\n{day2} Day: {list[2]}\n\tNight: {list[3]}\n\n{day3} Day: {list[4]}\n\tNight: {list[5]}\n\n{day4} Day: {list[6]}\n\t\
	Night: {list[7]}\n\n{day5} Day: {list[8]}\n\tNight: {list[9]}\n\n{day6} Day: {list[10]}\n\tNight: {list[11]}\n\n{day7} Day: {list[12]}\n\tNight: {list[13]}\n\n{day8}\
	 Day: {list[14]}\n\tNight: {list[15]}')

print(g)

file = open("weather-op.txt","w")
file.write("This week's weather \n")
file.writelines(g)
file.close()