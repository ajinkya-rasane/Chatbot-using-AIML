import aiml
import os
import wikipedia
import requests

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
	kernel.bootstrap(brainFile = "bot_brain.brn")
else:
	kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
	kernel.saveBrain("bot_brain.brn")
wiki = 'abcd'
weather = 'bcdf'
# kernel now ready for use
while True:
	message = input("Enter your message >> ")
	if message == "quit":
		exit()
	elif message == "save":
		kernel.saveBrain("bot_brain.brn")
	else:
		bot_response = kernel.respond(message)
		if bot_response[0:4] == wiki:
			query = bot_response[5:]
			print(wikipedia.summary(query,sentences = 2))
		elif bot_response[0:4] == weather:
			query = bot_response[5:]
			api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0eac9a4df1582ed4070874b364a41343&q='
			city=query
			url=api_address+city
			jason_data=requests.get(url).json();
			main = jason_data['weather'][0]['main']
			cur_temp = jason_data['main']['temp']
			temp_max = jason_data['main']['temp_max']
			temp_min = jason_data['main']['temp_min']
			wind = jason_data['wind']['speed']
			humidity = jason_data['main']['humidity']
			print ("city+:",main)
			print ("temp:",cur_temp-273.15)
			print ("High:",temp_max-273.15)
			print ("Low :",temp_min-273.15)
			print ("Humidity(%):",humidity)
			print ("Wind Speed(km/h) :",wind)
		else:
			print(bot_response)
        	