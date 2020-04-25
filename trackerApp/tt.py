import requests,json

def news():
	heads=[]
	links=[]

	news = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=d6c5c5ac9cee4cfab940cc92c7d9f720')
	data = news.json()

	for i in range(len(data['articles'])):
		url = data['articles'][i]['url']
		articles = data['articles'][i]['title']

		if ('covid-19' in articles) or ('coronavirus' in articles) or ('COVID-19' in articles) or ('Coronavirus' in articles):
			heads.append(articles)
			links.append(url)

	datas = list(zip(heads,links))
	print(datas)
news()
