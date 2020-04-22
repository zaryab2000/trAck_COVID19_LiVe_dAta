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
	data = {'Afghanistan': 1176, 'Albania': 634, 'Algeria': 2910, 'Andorra': 717, 'Angola': 24, 'Antigua and Barbuda': 24, 'Argentina': 3144, 'Armenia': 1473, 'Australia': 6547, 'Austria': 14925, 'Azerbaijan': 1518, 'Bahamas': 65, 'Bahrain': 2009, 'Bangladesh': 3772, 'Barbados': 75, 'Belarus': 7281, 'Belgium': 41889, 'Belize': 18, 'Benin': 54, 'Bhutan': 6, 'Bolivia': 609, 'Bosnia and Herzegovina': 1368, 'Botswana': 22, 'Brazil': 43592, 'Brunei': 138, 'Bulgaria': 1024, 'Burkina Faso': 600, 'Burma': 121, 'Burundi': 11, 'Cabo Verde': 73, 'Cambodia': 122, 'Cameroon': 1163, 'Canada': 39598, 'Central African Republic': 14, 'Chad': 33, 'Chile': 11296, 'China': 83868, 'Colombia': 4149, 'Congo (Brazzaville)': 165, 'Congo (Kinshasa)': 359, 'Costa Rica': 669, "Cote d'Ivoire": 0, 'Croatia': 1950, 'Cuba': 1189, 'Cyprus': 790, 'Czechia': 7087, 'Denmark': 8108, 'Diamond Princess': 712, 'Djibouti': 974, 'Dominica': 16, 'Dominican Republic': 5300, 'Ecuador': 10398, 'Egypt': 3490, 'El Salvador': 237, 'Equatorial Guinea': 83, 'Eritrea': 39, 'Estonia': 1559, 'Eswatini': 31, 'Ethiopia': 116, 'Fiji': 18, 'Finland': 4129, 'France': 159315, 'Gabon': 156, 'Gambia': 0, 'Georgia': 416, 'Germany': 149044, 'Ghana': 1154, 'Greece': 2408, 'Grenada': 14, 'Guatemala': 316, 'Guinea': 761, 'Guinea-Bissau': 50, 'Guyana': 67, 'Haiti': 58, 'Holy See': 9, 'Honduras': 510, 'Hungary': 2168, 'Iceland': 1785, 'India': 20471, 'Indonesia': 7418, 'Iran': 85996, 'Iraq': 1631, 'Ireland': 16040, 'Israel': 14326, 'Italy': 187327, 'Jamaica': 233, 'Japan': 11512, 'Jordan': 428, 'Kazakhstan': 2070, 'Kenya': 303, 'Korea, South': 10694, 'Kosovo': 510, 'Kuwait': 2248, 'Kyrgyzstan': 612, 'Laos': 19, 'Latvia': 761, 'Lebanon': 682, 'Liberia': 101, 'Libya': 59, 'Liechtenstein': 81, 'Lithuania': 1370, 'Luxembourg': 3618, 'MS Zaandam': 9, 'Madagascar': 121, 'Malawi': 23, 'Malaysia': 5532, 'Maldives': 86, 'Mali': 293, 'Malta': 444, 'Mauritania': 7, 'Mauritius': 329, 'Mexico': 9501, 'Moldova': 2778, 'Monaco': 94, 'Mongolia': 35, 'Montenegro': 315, 'Morocco': 3377, 'Mozambique': 41, 'Namibia': 16, 'Nepal': 45, 'Netherlands': 35026, 'New Zealand': 1451, 'Nicaragua': 10, 'Niger': 657, 'Nigeria': 782, 'North Macedonia': 1259, 'Norway': 7275, 'Oman': 1614, 'Pakistan': 10076, 'Panama': 4821, 'Papua New Guinea': 8, 'Paraguay': 213, 'Peru': 17837, 'Philippines': 6710, 'Poland': 10169, 'Portugal': 21982, 'Qatar': 7141, 'Romania': 9710, 'Russia': 57999, 'Rwanda': 150, 'Saint Kitts and Nevis': 15, 'Saint Lucia': 15, 'Saint Vincent and the Grenadines': 13, 'San Marino': 488, 'Sao Tome and Principe': 4, 'Saudi Arabia': 12772, 'Senegal': 442, 'Serbia': 6630, 'Seychelles': 11, 'Sierra Leone': 61, 'Singapore': 10141, 'Slovakia': 1244, 'Slovenia': 1353, 'Somalia': 286, 'South Africa': 3465, 'South Sudan': 4, 'Spain': 208389, 'Sri Lanka': 323, 'Sudan': 140, 'Suriname': 10, 'Sweden': 16004, 'Switzerland': 28268, 'Syria': 42, 'Taiwan*': 426, 'Tanzania': 284, 'Thailand': 2826, 'Timor-Leste': 23, 'Togo': 88, 'Trinidad and Tobago': 115, 'Tunisia': 901, 'Turkey': 95591, 'US': 830789, 'Uganda': 61, 'Ukraine': 6592, 'United Arab Emirates': 8238, 'United Kingdom': 134635, 'Uruguay': 543, 'Uzbekistan': 1692, 'Venezuela': 288, 'Vietnam': 268, 'West Bank and Gaza': 474, 'Western Sahara': 6, 'Yemen': 1, 'Zambia': 74, 'Zimbabwe': 28}
	new_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)[:10]}
	print('+'*60)
	print(new_data)
sorting()






















































