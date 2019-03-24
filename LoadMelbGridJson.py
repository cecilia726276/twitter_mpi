import json
from MelbGrid import MelbGrid
def loadMelbGridJson(fileName):
    file = open(fileName, encoding='utf-8')
    melbJson = json.load(file)
    return melbJson

if __name__ == "__main__":
    fn = "melbGrid.json"
    gridJson = loadMelbGridJson(fn)
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
    #print(type(gridObjList[0].xmin))   xmin is float, id is str
    for obj in gridObjList:
        print("id = %s xmin = %f xmax = %f ymin = %f ymax = %f" % (obj.id, obj.xmin, obj.xmax, obj.ymin, obj.ymax))
