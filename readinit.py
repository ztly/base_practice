import configparser


class ReadIni:
    def __init__(self):
        self.data = self.loadIni()

    def loadIni(self):
        cf = configparser.ConfigParser()
        cf.read('/Users/edz/Documents/VS_Code/BaseImooc/config/LocalElement.ini')
        return cf

    def get_value(self, key):
        info = self.data.get('element', key)
        return info


'''if __name__ == "__main__":
    read_ini = ReadIni()
    print(read_ini.get_value('username'))'''
read_ini = ReadIni()
