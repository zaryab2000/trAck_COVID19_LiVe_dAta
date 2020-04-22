import requests,json
from django.shortcuts import render


def index(request):
	return render(request, 'trackerApp/base.html')

def getCountries():
	country_url = f'https://covid19.mathdro.id/api/countries'
	countries_list=[]

	country_data = requests.get(country_url)
	con_json=country_data.json()

	countries=con_json['countries']

	for country in countries:
		name = country['name']
		countries_list.append(name)

	return countries_list

def data(request):
	url = f'https://covid19.mathdro.id/api/'

	data = requests.get(url)

	json=data.json()

	confirmed = json['confirmed']['value']
	recover  =json['recovered']['value']
	deaths = json['deaths']['value']

	context = {
		'confirmed':confirmed,
		'recovered':recover,
		'deaths':deaths,
	}
	return render(request,'trackerApp/data.html', context)

	
def getCountryData(request):
	countries_list=getCountries()

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

def top(request):
	countries=[]
	vals=[]
	init_list={}

	# cont_list = getCountries()

	# for name in cont_list:
	# 	country_url = f'https://covid19.mathdro.id/api/countries/{name}'
	# 	cont_data = requests.get(country_url)
	# 	json=cont_data.json()

	# 	try:
	# 		conf = json['confirmed']['value']
	# 	except KeyError:
	# 		conf = 0

	# 	init_list[name]=conf
	# new_data = {k: v for k, v in sorted(init_list.items(), key=lambda item: item[1], reverse=True)[:10]}
	new_data= {'US': 834858, 'Spain': 208389, 'Italy': 187327, 'France': 159315, 'Germany': 149401, 'United Kingdom': 134637, 'Turkey': 98674, 'Iran': 85996, 'China': 83868, 'Russia': 57999}

	for key,value in new_data.items():
		countries.append(key)
		vals.append(value)
	context={
		'countries':countries,
		'value':vals
	}

	return render(request, 'trackerApp/top10.html',context)






















