import requests
from bs4 import BeautifulSoup

file = requests.get("https://weather.com/en-IN/weather/tenday/l/dc3606bad8fa1360d11e515d0e06312e1a9ccd318c216935521c7cce6c362cdf")

soup = BeautifulSoup(file.content, "html.parser")

#content = soup.find(class_ = "card Card--card--2AzRg DailyForecast--Card--1WBkh")
list= []
for word in soup.find_all('p'):
	content=word.get_text()

	list.append(content)
