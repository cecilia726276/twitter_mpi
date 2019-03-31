# extract coordinates and hashtags from lines
import json
import re


def regex(str):
	# sbatch xxx.slurm
	# sbatch --array=1-10
	# squeue -u lev
	coordinates = None
	hashtags = None
	try:
		str_dict = json.loads(str)
		if "value" in str_dict:
			if "geometry" in str_dict["value"]:
				if "coordinates" in str_dict["value"]["geometry"]:
					coordinates = str_dict["value"]["geometry"]["coordinates"]
		if "doc" in str_dict:
			if "entities" in str_dict["doc"]:
				if "hashtags" in str_dict["doc"]["entities"]:
					hashtags = str_dict["doc"]["entities"]["hashtags"]

	except Exception:
		print("None to match")
		return None, None
	else:
		return coordinates, hashtags
'''
if __name__ == "__main__":
	# with open("tinyTwitter.json", "r", encoding='UTF-8') as file:
	with open("jsonTest.json", "r", encoding='UTF-8') as file:
		line = file.readline()

		while line:
			m_list = regex(line[:-2])
			print("coor:")
			print(type(m_list[0][1]))
			print(m_list[0][1])
			print("hashtags text:")
			#print(type(m_list[1]))
			#print(m_list[1])

			if len(m_list[1]) > 0:
				for j in range(0, len(m_list[1])):
					print(m_list[1][j]['text'])

			print("\n")
			line = file.readline()
'''

