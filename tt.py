import json, requests

def getCountries():
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

	return countries_list

def top():

	init_list={}
	final_list=[]
	cont_list = getCountries()

	# country_url = f'https://covid19.mathdro.id/api/countries/India'
	# data = requests.get(country_url)
	# jsonn=data.json()
	# json = jsonn['confirmed']['value']
	for name in cont_list:
		country_url = f'https://covid19.mathdro.id/api/countries/{name}'
		cont_data = requests.get(country_url)
		json=cont_data.json()

		try:
			conf = json['confirmed']['value']
		except KeyError:
			conf = 0

		init_list[name]=conf

		# init_list.append(conf)


	print(init_list)

def sorting():
	dd = {'US': 834858, 'Spain': 208389, 'Italy': 187327, 'France': 159315, 'Germany': 149401, 'United Kingdom': 134637, 'Turkey': 98674, 'Iran': 85996, 'China': 83868, 'Russia': 57999}
	for key,value in dd.items():
		print(value)
		print(key)

sorting()






















































