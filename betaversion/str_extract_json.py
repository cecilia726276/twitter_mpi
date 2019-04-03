# extract coordinates and hashtags from lines
import json


def regex(string):

	coordinates = None
	hashtags = None
	if string[-1] == ',':
		string = string[:-1]
	try:
		str_dict = json.loads(string)
		if "doc" in str_dict:
			if "geo" in str_dict["doc"]:
				if "coordinates" in str_dict["doc"]["geo"]:
					coordinates = str_dict["doc"]["geo"]["coordinates"]
		if "doc" in str_dict:
			if "entities" in str_dict["doc"]:
				if "hashtags" in str_dict["doc"]["entities"]:
					hashtags = str_dict["doc"]["entities"]["hashtags"]

	except Exception:
		# print("None to match")
		return None, None
	else:
		return coordinates, hashtags