import subprocess
import os

class StubLoader:
    """Ta klasa jest uzywana do ladowania Stub do DUT"""

    #konstruktor klasy
    #stubPath - sciezka do lokacji w ktorej jest stub (bez nazwy pliku)
    #stubName - nazwa pliku wraz z rozszerzeniem
    #resultsOutput - sciezka do pliku do ktorego ma byc zapisany rezultat
    def __init__(self, stubPath, stubName, resultsOutput):
        self.stubPath = stubPath
        self.stubName = stubName
        self.resultsOutput = resultsOutput

    #metoda ktora wgrywa stuba.
    def loadStub(self):
        stubLocation = os.path.join(self.stubPath, self.stubName) #tworzy sciezke do pliku ze zstubem
        command = 'netboot --bootaxis -i '+stubLocation #komenda ktora zostanie wywylana w shellu
        try:
            process = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=10) #wywolanie komendy z zapisanie rezultatu do zmiennej
            with open(self.resultsOutput, 'w') as file: #zapis rezultatu do pliku
                file.write(str(process))
        except subprocess.TimeoutExpired: # wyjatek timeoutExpired wystapi jezeli DUT nie jest podlaczony lub jest juz zaprogramowany finnalFirmware
            with open(self.resultsOutput, 'w') as file:
                file.write("Time expired error")


    #metoda sprawdza czy istnieje plik ze stubem
    def checkIfExist(self):
        stubLocation = os.path.join(self.stubPath, self.stubName)
        print(stubLocation)
        exist = os.path.exists(stubLocation)
        return exist
