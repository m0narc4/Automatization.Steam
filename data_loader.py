import json
import os


class DataLoader:
    def __init__(self, config_path='D:/PythonProjects/TQuality_Task2/config.json', test_data_path='D:/PythonProjects/TQuality_Task2/test_data.json'):
        self.config_path = config_path
        self.test_data_path = test_data_path
        self.config_file = self.__load_config()
        self.test_data_file = self.__load_test_data()

    def __load_config(self):
        with open(self.config_path) as config_file:
            config = json.load(config_file)
        return config


    def __load_test_data(self):
        with open(self.test_data_path) as test_data_file:
            test_data = json.load(test_data_file)
        return test_data


    def get_test_data(self, key):
        return self.test_data_file[key]

    def get_config_data(self, key):
        return self.config_file[key]

    def get_all_config_data(self):
        return self.config_file

    def get_all_test_data(self):
        return self.test_data_file

