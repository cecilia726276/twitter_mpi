import json

def loadJsonFile(fileName):
    file = open(fileName, encoding='utf-8')
    list = []
    list = json.load(file)
    return list

if __name__ == "__main__":
    #fn = "jsonTest.json"
    fn = "tinyTwitterPretty.json"
    array = loadJsonFile(fn)
    for block in array:
        print(block)
        print("\n")


