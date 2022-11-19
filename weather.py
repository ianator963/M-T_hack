import requests
from bs4 import BeautifulSoup

file = requests.get("https://weather.com/en-IN/weather/tenday/l/dc3606bad8fa1360d11e515d0e06312e1a9ccd318c216935521c7cce6c362cdf")

soup = BeautifulSoup(file.content, "html.parser")

#content = soup.find(class_ = "card Card--card--2AzRg DailyForecast--Card--1WBkh")
list= []
for word in soup.find_all('p'):
	content=word.get_text()

	list.append(content)
f = f'Day 1: Day: {list[0]} Day 1: Night: {list[1]}\nDay 2: Day: {list[2]} Day 2: Night: {list[3]}\nDay 3: Day: {list[4]} Day 3: Night: {list[5]}\nDay 4: Day: {list[6]} Day 4: Night: {list[7]}\nDay 5: Day: {list[8]} Day 5: Night: {list[9]}\nDay 6: Day: {list[10]} Day 6: Night: {list[11]}\nDay 7: Day: {list[12]} Day 7: Night: {list[13]}\nDay 8: Day: {list[14]} Day 8: Night: {list[15]}\nDay 9: Day: {list[16]} Day 9: Night: {list[17]}\nDay 10: Day: {list[18]} Day 10: Night: {list[19]}\nDay 11: Day: {list[20]} Day 11: Night: {list[21]}\nDay 12: Day: {list[22]} Day 12: Night: {list[23]}\nDay 13: Day: {list[24]} Day 13: Night: {list[25]}\nDay 14: Day: {list[26]} Day 14: Night: {list[27]}\nDay 15: Day: {list[28]} Day 15: Night: {list[29]}'

print(f)