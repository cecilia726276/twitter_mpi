import json
class MelbGrid(object):
    postCount = 0         # record the post count for each grid.
    hashtagsList = None # store the hashtags that belong to particular grid.

    def __init__(self, id, xmin, xmax, ymin, ymax):
        self.id = id
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.hashtagsList = dict()  # initialize object dictionary

    def updateHashtagsList(self, str):
        if str in self.hashtagsList.keys():
            self.hashtagsList[str] += 1
        else:
            newDict = {str: 1}
            self.hashtagsList.update(newDict)

    def addpostcount(self):
        self.postCount += 1

    def addhashtags(self, text):
        if text != None:
            self.updateHashtagsList(text)

    def checkInGrid(self, x, y): # each data line calls it by entering its x,y coordinates,and hashtags' text
                                       # the outcome is to update each grid object's postCount and hashtagsList
        if self.id == "A1":
            if x >= self.xmin and x <= self.xmax and y >= self.ymin and y <= self.ymax:
                return True
        elif self.id == "A2" or self.id == "A3" or self.id == "A4" or self.id == "C5":
            if x > self.xmin and x <= self.xmax and y >= self.ymin and y <= self.ymax:
                return True
        elif self.id == "B1" or self.id == "C1" or self.id == "D3":
            if x >= self.xmin and x <= self.xmax and y >= self.ymin and y < self.ymax:
                return True
        else:    #"B2" "B3"  "B4" "C2" "C3"  "C4"  "D4"  "D5"
            if x > self.xmin and x <= self.xmax and y >= self.ymin and y < self.ymax:
                return True
        return False

def readMelbGrid(filename): # this function is used to load the MelbGrid objects from the file. return @list
                            # It's not necessary exist in this file
    file = open(filename, "rU")
    gridJson = json.load(file)
    features = []
    features = gridJson['features']
    gridObjList = []
    for feature in features:
        id = feature['properties']['id']
        xmin = feature['properties']['xmin']
        xmax = feature['properties']['xmax']
        ymin = feature['properties']['ymin']
        ymax = feature['properties']['ymax']
        melbGrid = MelbGrid(id, xmin, xmax, ymin, ymax)
        gridObjList.append(melbGrid)
        # print(type(gridObjList[0].xmin))   xmin is float, id is str
    return gridObjList

'''
if __name__ == "__main__": # use for testing
    gridList = readMelbGrid("melbGrid.json")
    for i in range(0, len(gridList)):
        if gridList[i].checkInGrid(145.08645638, -37.96924206, "abcd"): #(x,y,hashtags_text) if find one grid,then stop matching
            break

    for obj in gridList:
        print(obj.id)
        print(obj.postCount)
        print(obj.hashtagsList)

    # sort the hashtags from largest to lower for each grid
    #print(sorted(tagList.items(), key=lambda x: x[1], reverse=True))
'''


