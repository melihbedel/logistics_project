from core.app_data import ApplicationData
from datetime import datetime
import os

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
os.chdir(dir)

TIME_LOG = 'time_log.txt'
EVENT_LOG = 'event_log.txt'
INPUT_LOG = 'input_log.txt'

class FilesFactory:
    def __init__(self,data: ApplicationData):
        self._app_data = data
        self.set_initial_time()

    def update_time(self):
        self._app_data._current_time = datetime.now()

    def set_initial_time(self):
        f = open(TIME_LOG, 'a')
        f.write(datetime.now().strftime("%Y %m %d %H %M") + '\n')
        f.close()
        f = open(TIME_LOG,'r')
        line = f.readline().split()
        year, month, day, hour, minutes = line
        self._app_data._current_time = datetime(int(year), int(month), int(day), int(hour), int(minutes))

    def append_input_log(self, value):
        f = open(INPUT_LOG,'a')
        f.write(value + '\n')

    def append_event_log(self,value):
        f = open(EVENT_LOG, 'a')
        f.write(value + '\n')

    def read_input_log(self):
        f = open(INPUT_LOG, 'r')
        return f.readlines()
    
    def clear_event_log(self):
        open(EVENT_LOG, 'w').close()
