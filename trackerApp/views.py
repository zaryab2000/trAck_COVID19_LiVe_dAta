import requests,json
from django.shortcuts import render


def index(request):
	return render(request, 'trackerApp/base.html')

def data(request):
	url = f'https://covid19.mathdro.id/api/'
	country_url = f'https://covid19.mathdro.id/api/countries'

	countries_list=[]

	data = requests.get(url)
	country_data = requests.get(country_url)

	json=data.json()
	con_json=country_data.json()

	countries=con_json['countries']
	confirmed = json['confirmed']['value']
	recover  =json['recovered']['value']
	deaths = json['deaths']['value']

	for country in countries:
		name = country['name']
		countries_list.append(name)

	print(countries_list)
	context = {
		'confirmed':confirmed,
		'recovered':recover,
		'deaths':deaths,
		'names':countries_list
	}
	return render(request,'trackerApp/data.html', context)

	
def getCountryData(request):
	pass