import json, requests
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
print(getCountries())