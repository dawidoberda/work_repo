import subprocess
from StubLoader import StubLoader
from configparser import ConfigParser
import os
import logging
import datetime

def main():
    parser = ConfigParser()

    #parser.read('C:\\Users\\oberdad\\Desktop\\Dawid\\ProjektyMoje\\UniversalAxisTester\\universalCameraTester\\config.ini')

    parser.read('config.ini')

    stubPath = parser.get('settings', 'stubpath')
    stubName = parser.get('settings', 'stubname')
    resultsOutput = parser.get('settings', 'results_output_path')

    logFile = parser.get('settings', 'log_file_path')

    logging.basicConfig(filename=logFile, level=logging.INFO)

    stubInstance1 = StubLoader(stubPath, stubName, resultsOutput)

    exits = stubInstance1.checkIfExist()

    if exits:
        today = str(datetime.datetime.today())
        logging.info('{}:stub path is exist'.format(today))
    else:
        today = str(datetime.datetime.today())
        logging.info('{}:stub path is NOT exist'.format(today))

    if exits:
        print("Loading stub...")
        stubInstance1.loadStub()

        #TODO: dodac sprawdzanie zawartosci pliku stubLoadedResult.txt i jezeli sie zgadza to wyswietlic stub loaded i zapisac do log

main()