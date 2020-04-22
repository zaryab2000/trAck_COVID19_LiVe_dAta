import requests,json
from django.shortcuts import render


def index(request):
	return render(request, 'trackerApp/base.html')

def getCountries():
	countries_list=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Diamond Princess', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'MS Zaandam', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan*', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'US', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'West Bank and Gaza', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

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

	cont_list = getCountries()

	for name in cont_list:
		country_url = f'https://covid19.mathdro.id/api/countries/{name}'
		cont_data = requests.get(country_url)
		json=cont_data.json()

		try:
			conf = json['confirmed']['value']
		except KeyError:
			conf = 0

		init_list[name]=conf
	new_data = {k: v for k, v in sorted(init_list.items(), key=lambda item: item[1], reverse=True)[:10]}

	for key,value in new_data.items():
		countries.append(key)
		vals.append(value)
	context={
		'countries':countries,
		'value':vals
	}

	return render(request, 'trackerApp/top10.html',context)






















