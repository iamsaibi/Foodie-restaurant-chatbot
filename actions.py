from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import pip
failed = pip.main(["install", 'aiosmtplib'])

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib, ssl
import aiosmtplib
from email.message import EmailMessage

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
Cities = [
'Ahmedabad',
'Bengaluru',
'Chennai',
'Delhi',
'Hyderabad',
'Kolkata',
'Mumbai',
'Pune',
'Agra',
'Ajmer',
'Aligarh',
'Amravati',
'Amritsar',
'Asansol',
'Aurangabad',
'Bareilly',
'Belgaum',
'Bhavnagar',
'Bhiwandi',
'Bhopal',
'Bhubaneswar',
'Bikaner',
'Bilaspur',
'Bokaro Steel City',
'Chandigarh',
'Coimbatore',
'Cuttack',
'Dehradun',
'Dhanbad',
'Bhilai',
'Durgapur',
'Dindigul',
'Erode',
'Faridabad',
'Firozabad',
'Ghaziabad',
'Gorakhpur',
'Gulbarga',
'Guntur',
'Gwalior',
'Gurgaon',
'Guwahati',
'Hamirpur',
'Hubli',
'Indore',
'Jabalpur',
'Jaipur',
'Jalandhar',
'Jammu',
'Jamnagar',
'Jamshedpur',
'Jhansi',
'Jodhpur',
'Kakinada',
'Kannur',
'Kanpur',
'Karnal',
'Kochi',
'Kolhapur',
'Kollam',
'Kozhikode',
'Kurnool',
'Ludhiana',
'Lucknow',
'Madurai',
'Malappuram',
'Mathura',
'Mangalore',
'Meerut',
'Moradabad',
'Mysore',
'Nagpur',
'Nanded',
'Nashik',
'Nellore',
'Noida',
'Patna',
'Pondicherry',
'Purulia',
'Prayagraj',
'Raipur',
'Rajkot',
'Rajahmundry',
'Ranchi',
'Rourkela',
'Rishikesh',
'Ratlam',
'Salem',
'Sangli',
'Shimla',
'Siliguri',
'Solapur',
'Srinagar',
'Surat',
'Thanjavur',
'Thiruvananthapuram',
'Thrissur',
'Tiruchirappalli',
'Tirunelveli',
'Tiruvannamalai',
'Ujjain',
'Bijapur',
'Vadodara',
'Varanasi',
'Vijayawada',
'Visakhapatnam',
'Vellore',
'Warangal'
]
EmailContent = ""

def decodeBudget(budget:str, x):
	try:
		budget = float(budget)
	except:
		budget = str(budget)
	
	if(type(budget) == 'float'):
		if x == budget:
			return True
		return False

	if budget == 'low' and x <= 300:
		return True
	elif budget == 'mid' and x <= 700 and x > 300:
		return True
	elif budget == 'high' and x > 700:
		return True
	else: 
		return False
	

def RestaurantSearch(City,Cuisine, Rating=1.0, Budget=None, Price=None):
	temp = ZomatoData.copy()
	if Cuisine:
		temp = temp[temp['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())]
	if City:
		temp = temp[temp['City'].apply(lambda x: City.lower() in x.lower())]
	if Rating:
		temp = temp[temp['Aggregate rating'].apply(lambda x: x >= float(Rating))]
	if Budget:
		temp = temp[temp['Average Cost for two'].apply(lambda x: decodeBudget(Budget, x))]
	if Price[0] and Price[1]:
		temp = temp[temp['Average Cost for two'].apply(lambda x: x >= Price[0] and x <= Price[1])]
	if temp.shape[0] == 0:
		temp = pd.DataFrame(columns = ZomatoData.columns)
	return temp[['Restaurant Name','Address','Average Cost for two','Aggregate rating']].sort_values(by='Aggregate rating', ascending=False)

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		rating = tracker.get_slot('rating')
		price_l = tracker.get_slot('price_lowerbound')
		price_u = tracker.get_slot('price_upperbound')
		results = RestaurantSearch(City=loc,Cuisine=cuisine, Budget=budget, Rating=rating, Price= (price_l, price_u))
		response=""
		found=True
		if results.shape[0] == 0:
			response= "No restaurants found"
			found=False
		else:
			response = "Found ({}) places. Listing top results. \n".format(results.shape[0])
			for idx, restaurant in results[:5].iterrows():
				response = response + F"{restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
		
		global EmailContent
		EmailContent = "Found places. \n".format(results.shape[0])
		for idx, restaurant in results[:10].iterrows():
			EmailContent = EmailContent + F"{restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
		
		dispatcher.utter_message("-----")
		dispatcher.utter_message(response)
		return [SlotSet('restaurant_found',found)]

class ActionValidateLocation(Action):
	def name(self):
		return 'action_check_location'

	async def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		location_operable  = loc.lower() in list(map(lambda x: x.lower(), WeOperate)) 
		location_found = loc.lower() in list(map(lambda x: x.lower(), Cities))
		
		if location_found and not location_operable:
			return [SlotSet('valid_location','not_operable'),SlotSet('location',None)]
		elif not location_found and not location_operable:
			return [SlotSet('valid_location','not_found'),SlotSet('location',None)]
		
		return [SlotSet('valid_location','found'),SlotSet('location',loc)]



class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	async def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		sender_email = "upgradtest123@gmail.com"
		password = "Google.com1"
		receiver_email = MailID
		
		msg = EmailMessage()
		msg['Subject'] = 'Your preferred list of restaurants'
		msg['From'] = sender_email
		msg['To'] = receiver_email
		msg.set_content(EmailContent)
		smtp = aiosmtplib.SMTP("smtp.gmail.com", port=587)
		await smtp.connect()
		await smtp.starttls()
		await smtp.login(sender_email, password)
		await smtp.send_message(msg)
		await smtp.quit()
		print("Mail queued to send to {0}".format(MailID))
		dispatcher.utter_message("Mail queued to send to {0}. You will receive it shortly.".format(MailID))
		return [SlotSet('mail_id',MailID)]