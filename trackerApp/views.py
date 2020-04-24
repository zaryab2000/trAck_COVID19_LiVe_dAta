import requests,json
from bs4 import BeautifulSoup
from django.shortcuts import render,redirect
from django.core.paginator import Paginator



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
		try:

			name = request.POST.get('country_name')
			detail_url = f'https://covid19.mathdro.id/api/countries/{name}'
			
			country_detail = requests.get(detail_url)
			detail_json=country_detail.json()

			confirmed = detail_json['confirmed']['value']
			recover  =detail_json['recovered']['value']
			deaths = detail_json['deaths']['value']

			context = {
			'confirmed':confirmed,
			'recovered':recover,
			'deaths':deaths,
			'names':countries_list
			}
		except:
			return redirect('country_data')

	else:
		context = {
		'confirmed':0,
		'recovered':0,
		'deaths':0,
		'names':countries_list
	}

	return render(request, 'trackerApp/country_data.html',context)

def topConfirm(request):
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

	# ['US', 'Spain', 'Italy', 'France', 'Germany', 'United Kingdom', 'Turkey', 'Iran', 'China', 'Russia']
	# [842629, 208389, 187327, 157135, 150648, 134638, 98674, 85996, 83876, 57999]
	count = [1,2,3,4,5,6,7,8,9,10]
	data =list(zip(count,countries,vals))

	context={
		'data':data,
	}

	return render(request, 'trackerApp/top10.html',context)

def getNews(request):
	heads=[]
	source=[]
	news_list = []
	links = []
	
	response=requests.get('https://www.thehindu.com/news/national/')
	soup=BeautifulSoup(response.text,'html.parser')
	divs=soup.find_all('a',{'class':'Other-StoryCard-heading'})   

	for anch in divs:
		news_list.append(anch.text.strip())
		links.append(anch['href'])

	# links = ['https://www.thehindu.com/news/national/coronavirus-haryana-cancels-chinese-testing-kits-order/article31410500.ece', 'https://www.thehindu.com/news/national/allow-media-persons-to-cross-delhi-noida-border-with-photo-id-nba/article31410494.ece', 'https://www.thehindu.com/news/national/anaganwadi-workers-in-punjab-go-the-extra-mile-in-combating-covid-19/article31410480.ece', 'https://www.thehindu.com/news/national/ap-telangana-report-3-deaths-kerala-records-11-new-cases/article31411112.ece', 'https://www.thehindu.com/news/national/illicit-liquor-unit-unearthed-in-berhampur/article31410477.ece', 'https://www.thehindu.com/news/national/73-policemen-quarantined-after-five-moradabad-violence-accused-test-positive-for-covid-19/article31411068.ece', 'https://www.thehindu.com/news/national/no-new-covid-19-case-in-tripura/article31410475.ece', 'https://www.thehindu.com/news/national/police-exchange-fire-with-maoists-in-malkangiri/article31410472.ece', 'https://www.thehindu.com/news/national/less-than-1-wastage-in-fci-godowns-paswan/article31410716.ece', 'https://www.thehindu.com/news/national/central-vista-former-top-officers-of-mea-express-concern/article31410470.ece', 'https://www.thehindu.com/news/national/aadhaar-seeding-deadline-for-pm-kisan-extended-for-some-states/article31410468.ece', 'https://www.thehindu.com/news/national/jk-parties-slam-uapa-fir-against-journalist-geelani/article31410466.ece', 'https://www.thehindu.com/news/national/congress-seeks-legal-action-against-arnab-goswami/article31410712.ece', 'https://www.thehindu.com/news/national/let-there-be-no-illusion-that-covid-19-will-go-after-may-3-chhattisgarh-health-minister/article31410714.ece', 'https://www.thehindu.com/news/national/fake-gutka-seized-in-berhampur/article31410704.ece', 'https://www.thehindu.com/news/national/policemen-in-coronavirus-fight-have-no-insurance/article31409779.ece', 'https://www.thehindu.com/news/national/dont-deport-foreigners-engaged-in-tablighi-activities-centre/article31409696.ece', 'https://www.thehindu.com/news/national/coronavirus-indian-medical-association-withdraws-protest-planafter-assurance-from-centre/article31409537.ece', 'https://www.thehindu.com/news/national/bill-gates-hails-modis-leadership/article31409405.ece', 'https://www.thehindu.com/news/national/foreign-attendees-at-tablighi-jamaat-congregation-under-ed-lens/article31409378.ece', 'https://www.thehindu.com/news/national/centre-cuts-non-urea-fertilizer-subsidy/article31409104.ece', 'https://www.thehindu.com/news/national/no-100-quota-for-tribal-teachers-supreme-court/article31409071.ece', 'https://www.thehindu.com/news/national/centre-state-can-fix-sugarcane-price-says-supreme-court/article31409007.ece', 'https://www.thehindu.com/news/national/coronavirus-15000-crore-package-for-emergency-healthcare-system-approved/article31407284.ece', 'https://www.thehindu.com/news/national/coronavirus-india-gifts-23-tonnes-of-essential-medicines-to-nepal/article31406850.ece', 'https://www.thehindu.com/news/national/coronavirus-indias-covid-19-recovery-rate-improves-to-nearly-20/article31406333.ece', 'https://www.thehindu.com/news/national/coronavirus-attacks-on-health-workers-to-attract-up-to-7-years-in-prison/article31404910.ece', 'https://www.thehindu.com/news/national/second-batch-of-pilgrims-who-returned-from-iran-reach-ladakh/article31404893.ece', 'https://www.thehindu.com/news/national/in-pictures-pan-india-coronavirus-lockdown-enters-day-29/article31404030.ece', 'https://www.thehindu.com/news/national/coronavirus-aviation-ministry-employee-tests-positive/article31403611.ece', 'https://www.thehindu.com/news/national/agustawestland-chopper-case-sc-dismisses-interim-bail-plea-of-christian-michel/article31403563.ece', 'https://www.thehindu.com/news/national/india-co-sponsors-resolution-calling-for-equitable-access-to-covid-19-vaccines/article31403513.ece', 'https://www.thehindu.com/news/national/covid-19-rss-chief-bhagwat-to-deliver-online-address-on-sunday/article31403099.ece', 'https://www.thehindu.com/news/national/govt-using-rice-to-make-sanitizer-for-rich/article31403056.ece', 'https://www.thehindu.com/news/national/rahul-gandhi-calls-for-ideas-on-possible-msme-stimulus-package/article31403036.ece', 'https://www.thehindu.com/news/national/amit-shah-speaks-to-doctors/article31402888.ece', 'https://www.thehindu.com/news/national/pregnant-women-about-to-deliver-must-be-tested-for-covid-19-even-if-asymptomatic-says-icmr/article31402457.ece', 'https://www.thehindu.com/news/national/india-coronavirus-lockdown-april-22-2020-live-updates/article31402409.ece', 'https://www.thehindu.com/news/national/coronavirus-centre-continues-bengal-study/article31402367.ece', 'https://www.thehindu.com/news/national/militants-shot-dead-in-jks-shopian/article31402283.ece', 'https://www.thehindu.com/news/national/coronavirus-bihar-is-lagging-behind-says-tejashwi-yadav/article31400945.ece', 'https://www.thehindu.com/news/national/coronavirus-govt-protocol-to-allow-seamen-at-indian-ports-to-return/article31400848.ece']
# or 'Coronavirus' or 'covid19'
	for index in range(len(news_list)):
		if ('COVID-19' in news_list[index]) or ('Coronavirus' in news_list[index]): 
			heads.append(news_list[index])
			source.append(links[index])

	data = list(zip(heads,source))
	total = len(data)
	
	paginator = Paginator(data,5)
	page_number =  request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context={
		'data':data,
		'page':page_obj,
		'total':total
	}
	return render(request, 'trackerApp/news.html',context)




















