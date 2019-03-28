# extract coordinates and hashtags from lines
#import json
import re


def regex(str, pattNum):
	# pattern1 = r"\"geo\" :.+\"coordinates\" : \[ (.+?) \]"
	# sbatch xxx.slurm
	# sbatch --array=1-10
	# squeue -u lev
	if pattNum == 1: # extract the coordinates
		pattern = r"\"geo\" : { \"type\" : \"Point\", \"coordinates\" : \[ (.+?) \] }"
                #pattern = r"\"geo\" :.+\"coordinates\" : \[ (.+?) \]"
	else: # extract the hashtags
		pattern = r"hashtags.+text\" : \"(.+?)\""
	try:
		ms = re.findall(pattern, str)
	except Exception:
		print("null to match")
		return None
	else:
		return ms

'''
if __name__ == "__main__":
	# with open("tinyTwitter.json", "r", encoding='UTF-8') as file:
	with open("tinyTwitter.json", "r") as file:
		line = file.readline()
		print(type(line))
		while line:
			# print (line)
			m_list = regex(line, 1)
			# print(m_str)
			print(type(m_list))
			print(m_list)
			if m_list:

				coordList = m_list[0].split(', ')
				coord = [float(x) for x in coordList]
				print(coord)
			print ("\n")
			line = file.readline()
'''
