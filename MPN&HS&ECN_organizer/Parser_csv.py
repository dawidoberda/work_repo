import csv
import os

class ParserCsv:
    def __init__(self, first_file_name, second_file_name):
        self.first_file_name = first_file_name
        self.second_file_name = second_file_name

    def check_if_exist(self):
        file_exist_indicator = [False, False]

        exist_file_one = os.path.exists(self.first_file_name)

        if exist_file_one:
            file_exist_indicator[0] = True
        else:
            file_exist_indicator[0] = False

        exist_file_two = os.path.exists(self.second_file_name)

        if exist_file_two:
            file_exist_indicator[1] = True
        else:
            file_exist_indicator[1] = False

        return file_exist_indicator

    def create_first_temp(self):
        with open(self.first_file_namem, 'r') as f:
            csv_one = csv.reader(f, delimiter=',')
            #TODO: sprobowac teraz otworzyc obiekt (kolejny csv) do zapisu w ktorym do nowego pliku zapiszemy tylko te z 0 kolumna = 'ENG:ESD data'