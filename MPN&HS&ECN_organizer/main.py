#ENG:ESD data
from Parser_csv import ParserCsv

def main():
    first_file = 'MPN_previous (copy).csv'
    second_file = 'MPN_today (copy).csv'
    csv_parser = ParserCsv(first_file, second_file)

    indicators = []
    indicators = csv_parser.check_if_exist()
    print(indicators)


if __name__=='__main__':
    main()
