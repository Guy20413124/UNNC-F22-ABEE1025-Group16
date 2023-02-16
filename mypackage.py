import json
import pandas as pd
from StaticEplusEngine import run_eplus_model, convert_json_idf

class FindBest(object):
    def __init__(self, idf_path, output_dir,epjson_path, eplus_run_path,parameter_key):
        ######### load the JSON file into a JSON dict #########
        self.epjson_path = epjson_path
        with open(epjson_path) as epJSON:
            self.epjson_dict = json.load(epJSON)
        self.eplus_run_path = eplus_run_path
        self.idf_path = idf_path
        self.output_dir = output_dir
        self.parameter_key = parameter_key
        self.paremeter_val = 0
        self.mean_temperature = 0
        self.__SHGC = 0
        self.__U = 0
    
    def display(self):
        for key,value in self.epjson_dict.items():
            print(key,":",value)

    @property
    def MeanTemp(self):
        return self.mean_temperature

    @property
    def SHGC(self):
        return self.__SHGC
    
    @SHGC.setter
    def SHGC(self,SHGC_value):
        self.__SHGC = SHGC_value
        self.paremeter_val = SHGC_value

    @property
    def u(self):
        return self.__U
    
    @u.setter
    def u(self,U_value):
        self.__U = U_value
        self.paremeter_val = U_value

    def calculate_mean_temperature(self):
        inner_dict = self.epjson_dict
        for i in range(len(self.parameter_key)):
            if i < len(self.parameter_key) - 1:
                inner_dict = inner_dict[self.parameter_key[i]]
        inner_dict[self.parameter_key[-1]] = self.paremeter_val
        with open(self.epjson_path, 'w') as epjson:
            json.dump(self.epjson_dict, epjson)
        convert_json_idf(self.eplus_run_path, self.epjson_path)
        run_eplus_model(self.eplus_run_path, self.idf_path, self.output_dir)
        temperatures = pd.read_csv(self.output_dir+"/eplusout.csv").iloc[:,-1]
        self.mean_temperature = temperatures.mean(axis=0)


    