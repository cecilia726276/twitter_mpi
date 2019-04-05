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
		if "doc" in str_dict:
			if "geo" in str_dict["doc"]:
				if "coordinates" in str_dict["doc"]["geo"]:
					coordinates = str_dict["doc"]["geo"]["coordinates"]
		if "doc" in str_dict:
			if "text" in str_dict["doc"]:
				hashtags = str_dict["doc"]["text"]
				pattern = r"(?= (#.+?) )"
				matchList = re.findall(pattern, hashtags)

	except Exception:
		print("None to match")
		return None, None
	else:
		return coordinates, matchList

if __name__ == "__main__":
	# with open("tinyTwitter.json", "r", encoding='UTF-8') as file:
	with open("file-0.json", "r") as file:
		line = file.readline()
		line = file.readline()
		m_list = regex(line[:-2])
		print(m_list[0])
		print(type(m_list[1]))
		print(m_list[1])
		# print(line)
		'''
		while line:
			
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


# def regex(str):
# 	# sbatch xxx.slurm
# 	# sbatch --array=1-10
# 	# squeue -u lev
# 	coordinates = None
# 	hashtags = None
# 	try:
# 		str_dict = json.loads(str)
# 		if "value" in str_dict:
# 			if "geometry" in str_dict["value"]:
# 				if "coordinates" in str_dict["value"]["geometry"]:
# 					coordinates = str_dict["value"]["geometry"]["coordinates"]
# 		if "doc" in str_dict:
# 			if "entities" in str_dict["doc"]:
# 				if "hashtags" in str_dict["doc"]["entities"]:
# 					hashtags = str_dict["doc"]["entities"]["hashtags"]
#
# 	except Exception:
# 		print("None to match")
# 		return None, None
# 	else:
# 		return coordinates, hashtags
#
# if __name__ == "__main__":
# 	# with open("oldTinyTwitter.json", "r", encoding='UTF-8') as file:
# 	with open("tinyTwitter(updated).json", "r") as file:
# 		line = file.readline()
# 		line = file.readline()
# 		while line:
# 			print(line)
# 			m_list = regex(line[:-2])
# 			print("coor:")
# 			if m_list:
# 				print(m_list[0])
# 				# print(type(m_list[0][1]))
# 				# print(m_list[0][1])
# 				print("hashtags text:")
# 				print(type(m_list[1]))
# 				print(m_list[1])
#
# 			if len(m_list[1]) > 0:
# 				for j in range(0, len(m_list[1])):
# 					print(m_list[1][j]['text'])
#
# 			print("\n")
# 			line = file.readline()


