from models.constants.route_status import RouteStatus
from datetime import datetime, timedelta
from models.constants.distances import Distances
from models.truck import Truck
from models.constants.locations import Locations


class Route:

    def __init__(self, id: int, department_time: datetime, start_location, destination):
        self.check_valid_location(start_location)
        for dest in destination:
            self.check_valid_location(dest)
        self.check_valid_destination(start_location,dest)
        self._start_location = start_location
        self._destination = destination
        self._id = id
        self._department_time = department_time
        # Set the initial current location to the start
        self._current_location = start_location
        self.status = RouteStatus.PENDING  # Set the initial status to pending
        self._truck: Truck | None = None
        self._packages = []

    @property
    def start_location(self):
        return self._start_location

    @property
    def destination(self):
        return self._destination

    @property
    def id(self):
        return self._id

    @property
    def department_time(self):
        return self._department_time

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def current_location(self):
        return self._current_location

    @current_location.setter
    def current_location(self, value):
        if value not in self.destination and value != self.start_location:
            raise ValueError(f'Location {value} not in route')
        self._current_location = value

    @property
    def packages(self):
        return self._packages

    @property
    def truck(self):
        return self._truck
    
    @truck.setter
    def truck(self, input: Truck):
        self._truck = input

    @property
    def final_route(self):
        # reads the department time, calculates the other location's arrival time
        # returns a dicitonary with key - location, value - arrival time
        route = {}
        arrival_time = self.department_time
        route[self.start_location] = self.department_time
        for loc in self.destination:
            time_increment = int(
                self.distance) / 87
            arrival_time += timedelta(hours=time_increment)
            route[loc] = arrival_time
        return route

    @property
    def distance(self):
        sum = 0
        current_loc = self.start_location
        for loc in self.destination:
            sum += Distances.data[current_loc][loc]
            current_loc = loc
        return sum
    
    @property
    def arrival_time(self):
        return list(self.final_route.values())[-1]

    def __str__(self) -> str:
        result = f'Route #{self.id}' + f'\nStatus: {self.status.value}' + \
            f'\nCurrent Location:{self.current_location}'
        result += '\n-----'
        result += '\nLocation and time of arrival:'
        for key, value in self.final_route.items():
            result += f'\n{key} ({value.strftime("%Y/%m/%d, %H:%M")})'
        return result

    def check_valid_location(self, input):
        values = [member.value for member in Locations]
        if input not in values:
            raise ValueError(f'Location {input} is not valid')

    def check_valid_destination(self,start, dest:tuple):
        if start == dest[0] or start == dest:
            raise ValueError(f'Route cannot be created between {start} and {start}')