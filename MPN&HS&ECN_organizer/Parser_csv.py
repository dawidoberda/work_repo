import csv
import os


class ParserCsv:

    actual_line_qty_first = 0
    actual_line_qty_second = 0

    def __init__(self, first_file_name, second_file_name, compare_file_name):
        self.first_file_name = first_file_name
        self.second_file_name = second_file_name
        self.compare_file_name = compare_file_name

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
        with open(self.first_file_name, 'r') as f:
            csv_one = csv.reader(f, delimiter=',')
            first_file_name_part = self.first_file_name.split(".")
            first_name = first_file_name_part[0] + '_temp.csv'

            with open(first_name, 'w') as w:
                csv_write_one = csv.writer(w, delimiter=',')

                for line in csv_one:
                    actual_line_qty_first = actual_line_qty_first+1
                    if (line[0] == 'ENG:ESD data' and line[10] == 'Axis'):
                        csv_write_one.writerow(line)

    def create_second_temp(self):
        with open(self.second_file_name, 'r') as f2:
            csv_two = csv.reader(f2, delimiter=',')
            second_file_name_part = self.second_file_name.split(".")
            second_name = second_file_name_part[0] + '_temp.csv'

            with open(second_name, 'w') as w2:
                csv_write_two = csv.writer(w2, delimiter=',')

                for line in csv_two:
                    if (line[0] == 'ENG:ESD data' and line[10] == 'Axis'):
                        csv_write_two.writerow(line)

    def compare_csv(self):
        pass
        #print(actual_line_qty_first)
            #TODO: sprawdzic dlaeczego nie dziala zmienna klasowa.
        # Nastepnie sprawdzic ile lini ma plik 1 i 2 pamietac ze potrzebny jest jakis csv ktory bedzie zbieral dane z
        # kolejnych dni i je zapamietywal (sztucznie go stworzyc) i porowniaine 2 sasiadujacych dni ma byc zapisywane do tego pliku