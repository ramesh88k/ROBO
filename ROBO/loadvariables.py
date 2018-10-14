import configparser
import numpy as np

class loadinifile(object):
    def __init__(self, file_name='variable.ini'):
        parser = configparser.ConfigParser()
        parser.optionxform = str
        parser.read('../config/' + str(file_name))
        self.__config__ = {}
        for section in parser.sections():
            for key, value in parser.items(section):
                if type(eval(parser.get(section, key), {}, {}))!= list:
                    setattr(self,key,eval(parser.get(section, key), {}, {}))
                else:
                    try:setattr(self,key,np.array(eval(parser.get(section, key), {}, {})),dtype = float)
                    except:setattr(self,key,np.array(eval(parser.get(section, key), {}, {})))


# myvariables = loadinifile()
# print(type(myvariables.N))
# print(myvariables.N)
