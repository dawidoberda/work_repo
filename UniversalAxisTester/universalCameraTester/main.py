from StubLoader import StubLoader
from configparser import ConfigParser
import logging
import datetime


if __name__ == '__main__':

    parser = ConfigParser()#tworzy obiekt parsera konfiguracji

    parser.read('config.ini')#wczytanie pliku z konfiguracja

    #czytanie ustawien z pliku konfiguracyjnego
    stubPath = parser.get('settings', 'stubpath')
    stubName = parser.get('settings', 'stubname')
    resultsOutput = parser.get('settings', 'results_output_path')
    logFile = parser.get('settings', 'log_file_path')

    #konfiguracja nowego loggera
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formmater = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler(logFile)
    file_handler.setFormatter(formmater)
    logger.addHandler(file_handler)

    #Obiekt klasy StubLoader do wgrywania stuba.
    #Jako argument przyjmuje sciazke do stuba, nazwe stuba oraz lokacje pliku do zapisywania rezultatu
    stubInstance1 = StubLoader(stubPath, stubName, resultsOutput)

    #motoda checkIfExist sprawdza czy istnieniej plik w podanej lokacji
    exits = stubInstance1.checkIfExist()

    #w zaleznosci od rezultatu logowanie odpowiedniej wiadomosci
    if exits:
        logger.info('Stub path is exist')
    else:
        logger.warning('Stub path is not exist !!')

    #ponizej nastepuje ladowanie stuba
    if exits:
        print("Loading stub...")
        stubInstance1.loadStub() #wywolanie metody load stub
        with open(resultsOutput, 'r') as file: #otwarcie pliku z rezultatem wgrania stuba i sprawdzenie rezultatu
            line = file.read() #wczytanie zawartosci pliku do zmiennej
            loadResult = line.find("Exiting with code 0") #sprawdzanie czy zmienna zawiera ciag znakow odpowiadajacy poprawnemu wgraniu stuba
            if loadResult !=-1: # motoda find zwraca -1 w przypadku braku znalezienia danego ciagu znakow
               print('Stub loaded successfully')
               logger.info('Stub loaded successfully')
            elif line == "Time expired error": #jezeli podczas wgrywania stuba wystapil wyjatek timeout to taki komunikat zostanie zapisany do pliku
                print("Time expired error - unable to find DUT")
                logger.warning("Time expired error - unable to find DUT")
            else:
                print('Stub loaded unsuccessfully')
                logger.warning('Stub loaded unsuccessfully')


