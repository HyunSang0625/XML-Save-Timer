# Time Again Module
import threading
import time
import json
import requests
import xmltodict
import xml.etree.ElementTree as ET

print("XML API include to JSON File Save")

# "인천국제공항" API XML File 30m Save
def rksi_time_again():
	def rksi():
		print("30m API XML File and JSON File Save")
		rksi_link = "http://amoapi.kma.go.kr/amoApi/metar?icao=RKSI"
		print(rksi_link)
		r = requests.get(rksi_link)
		root = ET.fromstring(r.text)
		tree = ET.ElementTree(root)
		tree.write("RKSI_weather.xml")
		doc = ET.parse("RKSI_weather.xml")
		print("API XML LINK => LOCAL XML SAVE")
		with open("RKSI_weather.xml", "r") as f:
			xmlString = f.read()
		print("XML Save File JSON File Change")
		jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
		print(jsonString)
		with open("RKSI_weather.json", "w") as f:	
			f.write(jsonString)
		print("Save XML to JSON File Change")
	threading.Timer(1800, rksi).start()
rksi_time_again()