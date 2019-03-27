# extract coordinates and hashtags from lines
import json
import re


def regex(str):
	pattern1 = r"\"geo\" : { \"type\" : \"Point\", \"coordinates\" : \[ (.+?) \] }"
	# pattern1 = r"\"geo\" :.+\"coordinates\" : \[ (.+?) \]"
	# sbatch xxx.slurm
	# sbatch --array=1-10
	# squeue -u lev

	pattern2 = r"hashtags.+text\" : \"(.+?)\""
	try:
		ms = re.findall(pattern1, str)
	except Exception:
		print("null to match")
		return None
	else:
		return ms


if __name__ == "__main__":
	# with open("tinyTwitter.json", "r", encoding='UTF-8') as file:
	with open("tinyTwitter.json", "r") as file:
		line = file.readline()
		print(type(line))
		while line:
			# print (line)
			m_list = regex(line)
			# print(m_str)
			print(type(m_list))
			print(m_list)
			if m_list:

				coordList = m_list[0].split(', ')
				coord = [float(x) for x in coordList]
				print(coord)
			print ("\n")
			line = file.readline()
