from pymongo import MongoClient
import sys

client = MongoClient()
db = client.ColbyHacksCBB

def parseDB(searchTerm):
	location = db.testImport.find({"placeName": searchTerm})
	list = ["place", "time", "description"]
	for document in location:
		place = document["placeName"]
		time = document["time"]
		description = document["eventString"]
		list = [ place, time, description ]
		returnString = list[2] + " at " + list[1]
		return returnString

	return "No Events"
