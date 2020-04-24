import requests,json


def top():
	countries=[]
	vals=[]
	init_list={}

	cont_list=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Diamond Princess', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'MS Zaandam', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan*', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'US', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'West Bank and Gaza', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']


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

	print(countries)
	print(vals)


def news():
	heads=[]
	source=[]
	news_list = ['Coronavirus | Haryana cancels Chinese testing kits order','Allow media persons to cross Delhi-Noida border with photo ID: NBA', 'Anaganwadi workers in Punjab go the extra mile in combating COVID-19', 'A.P., Telangana report 3 deaths, Kerala records 11 new cases', 'Illicit liquor unit unearthed in Berhampur', '73 policemen quarantined after five Moradabad violence accused test positive for COVID-19', 'No new COVID-19 case in Tripura', 'Police exchange fire with Maoists in Malkangiri', 'Less than 1% wastage in FCI godowns: Paswan', 'Central Vista: former top officers of MEA express concern', 'Aadhaar seeding deadline for PM KISAN extended for some States', 'J&K parties slam UAPA FIR against journalist Geelani', 'Congress seeks legal action against Arnab Goswami for comments against Sonia Gandhi', 'Let there be no illusion that COVID-19 will go after May 3: Chhattisgarh Health Minister', 'Fake gutka seized in Berhampur', 'Policemen in coronavirus fight have no insurance', 'Don’t deport foreigners engaged in Tablighi activities: Centre', 'Coronavirus | Indian Medical Association withdraws protest planafter assurance from Centre', 'Coronavirus | Bill Gates hails Narendra Modi’s leadership', 'Coronavirus | Foreign attendees at Tablighi Jamaat congregation under ED lens', 'Centre cuts non-urea fertilizer subsidy', 'No 100% quota for tribal teachers: Supreme Court', 'Centre, State can fix sugarcane price, says Supreme Court', 'Coronavirus | Union Cabinet approves ₹15,000-crore package for COVID-19 emergency response, health system preparedness', 'Coronavirus | India gifts 23 tonnes of essential medicines to Nepal', 'Coronavirus | India’s COVID-19 recovery rate improves to nearly 20%', 'Coronavirus | Attacks on health workers to attract up to 7 years in prison', 'Second batch of pilgrims who returned from Iran reach Ladakh', 'In pictures | Pan-India Coronavirus lockdown enters day 29', 'Coronavirus: Aviation ministry employee tests positive', 'AgustaWestland chopper case: SC dismisses interim bail plea of Christian Michel', 'India co-sponsors resolution calling for equitable access to COVID-19 vaccines', 'COVID-19: RSS chief Mohan Bhagwat to deliver online address on Sunday', 'Poor ‘dying of hunger’, govt busy using rice to make sanitizer for rich: Rahul Gandhi', 'Rahul Gandhi calls for ideas on possible MSME stimulus package', 'IMA withdraws planned protest after assurance from Amit Shah', 'Pregnant women about to deliver must be tested for COVID-19 even if asymptomatic, says ICMR', 'Coronavirus India lockdown Day 29 updates | April 22, 2020', 'Coronavirus | Centre continues Bengal study', 'Four militants shot dead in J&K’s Shopian', 'Coronavirus | Bihar is lagging behind, says Tejashwi Yadav', 'Coronavirus | Govt protocol to allow seamen at Indian ports to return', 'Coronavirus | COVID 19- toll rises to 15 in Bengal, NICED withdraws faulty testing kits']
	word_list = ['covid19, COVID-19', 'Coronavirus', 'virus', 'disease']
	links = ['https://www.thehindu.com/news/national/coronavirus-haryana-cancels-chinese-testing-kits-order/article31410500.ece', 'https://www.thehindu.com/news/national/allow-media-persons-to-cross-delhi-noida-border-with-photo-id-nba/article31410494.ece', 'https://www.thehindu.com/news/national/anaganwadi-workers-in-punjab-go-the-extra-mile-in-combating-covid-19/article31410480.ece', 'https://www.thehindu.com/news/national/ap-telangana-report-3-deaths-kerala-records-11-new-cases/article31411112.ece', 'https://www.thehindu.com/news/national/illicit-liquor-unit-unearthed-in-berhampur/article31410477.ece', 'https://www.thehindu.com/news/national/73-policemen-quarantined-after-five-moradabad-violence-accused-test-positive-for-covid-19/article31411068.ece', 'https://www.thehindu.com/news/national/no-new-covid-19-case-in-tripura/article31410475.ece', 'https://www.thehindu.com/news/national/police-exchange-fire-with-maoists-in-malkangiri/article31410472.ece', 'https://www.thehindu.com/news/national/less-than-1-wastage-in-fci-godowns-paswan/article31410716.ece', 'https://www.thehindu.com/news/national/central-vista-former-top-officers-of-mea-express-concern/article31410470.ece', 'https://www.thehindu.com/news/national/aadhaar-seeding-deadline-for-pm-kisan-extended-for-some-states/article31410468.ece', 'https://www.thehindu.com/news/national/jk-parties-slam-uapa-fir-against-journalist-geelani/article31410466.ece', 'https://www.thehindu.com/news/national/congress-seeks-legal-action-against-arnab-goswami/article31410712.ece', 'https://www.thehindu.com/news/national/let-there-be-no-illusion-that-covid-19-will-go-after-may-3-chhattisgarh-health-minister/article31410714.ece', 'https://www.thehindu.com/news/national/fake-gutka-seized-in-berhampur/article31410704.ece', 'https://www.thehindu.com/news/national/policemen-in-coronavirus-fight-have-no-insurance/article31409779.ece', 'https://www.thehindu.com/news/national/dont-deport-foreigners-engaged-in-tablighi-activities-centre/article31409696.ece', 'https://www.thehindu.com/news/national/coronavirus-indian-medical-association-withdraws-protest-planafter-assurance-from-centre/article31409537.ece', 'https://www.thehindu.com/news/national/bill-gates-hails-modis-leadership/article31409405.ece', 'https://www.thehindu.com/news/national/foreign-attendees-at-tablighi-jamaat-congregation-under-ed-lens/article31409378.ece', 'https://www.thehindu.com/news/national/centre-cuts-non-urea-fertilizer-subsidy/article31409104.ece', 'https://www.thehindu.com/news/national/no-100-quota-for-tribal-teachers-supreme-court/article31409071.ece', 'https://www.thehindu.com/news/national/centre-state-can-fix-sugarcane-price-says-supreme-court/article31409007.ece', 'https://www.thehindu.com/news/national/coronavirus-15000-crore-package-for-emergency-healthcare-system-approved/article31407284.ece', 'https://www.thehindu.com/news/national/coronavirus-india-gifts-23-tonnes-of-essential-medicines-to-nepal/article31406850.ece', 'https://www.thehindu.com/news/national/coronavirus-indias-covid-19-recovery-rate-improves-to-nearly-20/article31406333.ece', 'https://www.thehindu.com/news/national/coronavirus-attacks-on-health-workers-to-attract-up-to-7-years-in-prison/article31404910.ece', 'https://www.thehindu.com/news/national/second-batch-of-pilgrims-who-returned-from-iran-reach-ladakh/article31404893.ece', 'https://www.thehindu.com/news/national/in-pictures-pan-india-coronavirus-lockdown-enters-day-29/article31404030.ece', 'https://www.thehindu.com/news/national/coronavirus-aviation-ministry-employee-tests-positive/article31403611.ece', 'https://www.thehindu.com/news/national/agustawestland-chopper-case-sc-dismisses-interim-bail-plea-of-christian-michel/article31403563.ece', 'https://www.thehindu.com/news/national/india-co-sponsors-resolution-calling-for-equitable-access-to-covid-19-vaccines/article31403513.ece', 'https://www.thehindu.com/news/national/covid-19-rss-chief-bhagwat-to-deliver-online-address-on-sunday/article31403099.ece', 'https://www.thehindu.com/news/national/govt-using-rice-to-make-sanitizer-for-rich/article31403056.ece', 'https://www.thehindu.com/news/national/rahul-gandhi-calls-for-ideas-on-possible-msme-stimulus-package/article31403036.ece', 'https://www.thehindu.com/news/national/amit-shah-speaks-to-doctors/article31402888.ece', 'https://www.thehindu.com/news/national/pregnant-women-about-to-deliver-must-be-tested-for-covid-19-even-if-asymptomatic-says-icmr/article31402457.ece', 'https://www.thehindu.com/news/national/india-coronavirus-lockdown-april-22-2020-live-updates/article31402409.ece', 'https://www.thehindu.com/news/national/coronavirus-centre-continues-bengal-study/article31402367.ece', 'https://www.thehindu.com/news/national/militants-shot-dead-in-jks-shopian/article31402283.ece', 'https://www.thehindu.com/news/national/coronavirus-bihar-is-lagging-behind-says-tejashwi-yadav/article31400945.ece', 'https://www.thehindu.com/news/national/coronavirus-govt-protocol-to-allow-seamen-at-indian-ports-to-return/article31400848.ece']

	result = [head for head in news_list if 'COVID-19' or 'Coronavirus' or 'covid19' in head]
	for index in range(len(news_list)):
		if 'COVID-19' in news_list[index]:
			heads.append(news_list[index])
			source.append(links[index])


	print(heads)
	print(source)
news()