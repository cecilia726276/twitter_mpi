class MelbGrid(object):
    postCount = 0         # record the post count for each grid.
    hashtagsList = dict() # store the hashtags that belong to particular grid.

    def __init__(self, id, xmin, xmax, ymin, ymax):
        self.id = id
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def updateHashtagsList(self, text):
        if text in self.hashtagsList.keys():
            self.hashtagsList[text] += 1
        else:
            newDict = {text: 1}
            self.hashtagsList.update(newDict)
        return self.hashtagsList

    def checkInGrid(self, x, y): # wait for discussion
        if x >= self.xmin and x <= self.xmax and y >= self.ymin and y <= self.ymax:
            self.postCount += 1

if __name__ == "__main__": # use for testing
    testObj = MelbGrid("A1",0,0,0,0)
    for i in range(0, 1):
        MelbGrid.updateHashtagsList(testObj, "abc")

    MelbGrid.updateHashtagsList(testObj, "def")
    tagList = MelbGrid.updateHashtagsList(testObj, "def")
    print(tagList)
    # sort the hashtags from largest to lower for each grid
    print(sorted(tagList.items(), key=lambda x: x[1], reverse=True))
