#ENG:ESD data
from Parser_csv import ParserCsv

def main():
    first_file = 'MPN_previous (copy).csv'
    second_file = 'MPN_today (copy).csv'
    mpn_compare_file = 'MPN_compare.csv'
    csv_parser_mpn = ParserCsv(first_file, second_file, mpn_compare_file)

    indicators = []
    indicators = csv_parser_mpn.check_if_exist()
    print(indicators)

    if indicators[0] == True:
        csv_parser_mpn.create_first_temp()

    if indicators[1] == True:
        csv_parser_mpn.create_second_temp()


if __name__=='__main__':
    main()
