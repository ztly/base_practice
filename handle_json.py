import json

class HandleJson:
    def readJson(self):
        with open('/Users/edz/Documents/VS_Code/BaseImooc/config/cookie.json') as fp:
            data = json.load(fp)[4]
            print('datad的type:', type(data))
            print(data)
            return data

    def getData(self):
        return self.readJson()

    def writeJson(self, data):
        with open('/Users/edz/Documents/VS_Code/BaseImooc/config/cookie.json','w') as fp:
            fp.write(json.dumps(data))

handlejson = HandleJson()

