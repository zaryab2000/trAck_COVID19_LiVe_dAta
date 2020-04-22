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
	country_url = f'https://covid19.mathdro.id/api/countries'
	countries_list=[]

	country_data = requests.get(country_url)
	con_json=country_data.json()

	countries=con_json['countries']
	# confirmed = json['confirmed']['value']
	# recover  =json['recovered']['value']
	# deaths = json['deaths']['value']

	for country in countries:
		name = country['name']
		countries_list.append(name)

	if request.method =='POST':
		name = request.POST.get('country_name')
		detail_url = f'https://covid19.mathdro.id/api/countries/{name}'
		
		country_detail = requests.get(detail_url)
		detail_json=country_detail.json()

		confirmed = detail_json['confirmed']['value']
		recover  =detail_json['recovered']['value']
		deaths = detail_json['deaths']['value']

		print(name)

		context = {
		'confirmed':confirmed,
		'recovered':recover,
		'deaths':deaths,
		'names':countries_list
		}

	else:
		context = {
		'confirmed':0,
		'recovered':0,
		'deaths':0,
		'names':countries_list
	}

	return render(request, 'trackerApp/country_data.html',context)