from configparser import ConfigParser

config = ConfigParser()


config['settings'] = {
    'stubPath': 'C:\\Users\\oberdad\\Desktop\\Dawid\\TE\\Axis\\Stubs',
    'stubname': 'P7304_8.40_alpha5_2_kimagev2.bin',
    'log_file_path': 'C:\\Users\\oberdad\\Desktop\\Dawid\\ProjektyMoje\\UniversalAxisTester\\Temp\\Log.log',
    'results_output_path': 'C:\\Users\\oberdad\\Desktop\\Dawid\\ProjektyMoje\\UniversalAxisTester\\Temp\\stubLoadedResult.txt'
}

with open('config.ini', 'w') as f:
    config.write(f)