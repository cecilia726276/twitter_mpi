# extract coordinates and hashtags from lines
import json
import re

def regex(str):
	pattern1 = r"geo\".+\"coordinates\" : \[ (.+?) \]"
	pattern2 = r"hashtags.+text\" : \"(.+?)\""
	try:
		ms = re.findall(pattern2, str)
	except Exception:
		print("null to match")
		return None
	else:
		return ms
	
if __name__ == "__main__":
	

	with open("tinyTwitter.json", "r", encoding='UTF-8') as file:
		line = file.readline()
		print(type(line))
		while line:
			#print (line)
			m_list = regex(line)
			#print(m_str)
			print(type(m_list))
			print(m_list)
			print ("\n")

			line = file.readline()
			