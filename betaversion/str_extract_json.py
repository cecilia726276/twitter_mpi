# extract coordinates and hashtags from lines
import json
import re


def regex(string):
    coordinates = None
    matchlist = None
    # To avoid invalid reading of the last object of json file.
    if string[-1] == ',':
        string = string[:-1]
    try:
        # extract coordinates
        str_dict = json.loads(string)
        if "doc" in str_dict:
            if "geo" in str_dict["doc"]:
                if "coordinates" in str_dict["doc"]["geo"]:
                    coordinates = str_dict["doc"]["geo"]["coordinates"]
        # extract the text field for things that look like " #<STRING> " using regular expression
        if "doc" in str_dict:
            if "text" in str_dict["doc"]:
                hashtags = str_dict["doc"]["text"]
                pattern = r"(?= (#.+?) )"
                matchlist = re.findall(pattern, hashtags)

    except Exception:
        return None, None
    else:
        return coordinates, matchlist
