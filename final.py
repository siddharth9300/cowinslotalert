import requests
from datetime import datetime
import time

base_cowin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
api_url_telegram = "https://api.telegram.org/bot1219050631:AAF886aYpzIZnIk8me7bVbmCvXNpaoFD_mw/sendMessage?chat_id=@__groupid__&text="
group_id = "vaccine452005"
# delhi_district_ids = [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150] 
pincode_near = [452005,452006]

def fetch_data_from_cowin(pincodes):
	query_params = "?pincode={}&date={}".format(pincodes, today_date)
	headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
	final_url = base_cowin_url+query_params
	response = requests.get(final_url, headers=headers)
	extract_availability_data(response)
	# print(response.text)


def fetch_data_for_state(district_ids):
	for district_id in district_ids:
		fetch_data_from_cowin(district_id)

def extract_availability_data(response):
	response_json = response.json()
	for center in response_json["centers"]:
		for session in center["sessions"]:
			if session["available_capacity_dose1"] > 0  or session["available_capacity_dose1"] > 0 and session["min_age_limit"]==18: # edit age limt and slots 
			

				# message = " \n Name: {},\n Address: {},Pincode: {},\n Dose 1 Available: {},\n Minimum Age: {},\n Vaccine: {},\n Slots: {},\n Date: {},\n Book Here : https://selfregistration.cowin.gov.in/" .format(
				# 	center["name"],
				# 	center["address"], 
				# 	center["pincode"], 
				# 	session["available_capacity_dose1"],
				# 	session["min_age_limit"],
				# 	session["vaccine"],
				# 	session["slots"],
				# 	session["date"]

				message = " \n {} \n Address: {} \n\n Pin: {}\n\n Minimum Age: {}\n\n Vaccine: {}\n\n Slots: {}\n\n Total {} slots are available on \n  {}\n\n Dose 1 Available: {}\n\n Dose 2 Available: {}\n\n COWIN : https://selfregistration.cowin.gov.in/" .format(
					center["name"],
					center["address"],
					center["pincode"],
					session["min_age_limit"],
					session["vaccine"],
					session["slots"],
					session["available_capacity"],
					session["date"],
					session["available_capacity_dose1"],
					session["available_capacity_dose2"]
					
				)
				send_message_telegram(message)

def send_message_telegram(message):
	final_telegram_url = api_url_telegram.replace("__groupid__", group_id)
	final_telegram_url = final_telegram_url + message
	response = requests.get(final_telegram_url)
	print(response)

a=0
if __name__ == "__main__":
	while True:
		a=a+1
		print("Searching for..",a," time")
		fetch_data_for_state(pincode_near)
		
