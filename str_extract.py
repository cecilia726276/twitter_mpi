# extract coordinates and hashtags from lines
import json
import re


def regex(str, pattNum):
	# pattern1 = r"\"geo\" :.+\"coordinates\" : \[ (.+?) \]"
	# sbatch xxx.slurm
	# sbatch --array=1-10
	# squeue -u lev
	if pattNum == 1: # extract the coordinates
		pattern = r"\"geometry\":{\"type\":\"Point\",\"coordinates\":\[(.+?)\]}"
	else: # extract the hashtags
		pattern = r"(\"hashtags\".+)*,\"urls\""
	try:
		ms = re.compile(pattern).findall(str)
	except Exception:
		print("null to match")
		return None
	else:
		return ms


if __name__ == "__main__":
	# with open("oldTinyTwitter.json", "r", encoding='UTF-8') as file:
	with open("tinyTwitter(updated).json", "r") as file:
		line = file.readline()
		i = 0;
		print(line)
		while line:
			i = i + 1;
			m_list = regex(line, 2)

			if m_list:
				mstr = "{" + m_list[0] + "}"
				print(mstr)
				hash_dict = eval(mstr)
				print(type(hash_dict))

				if hash_dict["hashtags"]:
					print(type(hash_dict["hashtags"][0]['text']))
					for j in range(0, len(hash_dict["hashtags"])):
						print(hash_dict["hashtags"][j]['text'])
					print("\n")

			# if m_list:
			# 	coordList = m_list[0].split(',')
			# 	coord = [float(x) for x in coordList]
			# 	print(coord)


			line = file.readline()
	print line
	print i

# There are 1002 lines and 1000 objects.

