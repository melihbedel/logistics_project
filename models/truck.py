from models.constants.truck_status import TruckStatus

class Truck:
    
    def __init__(self, id, name, capacity, max_range):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._max_range = max_range
        self._status = TruckStatus.FREE
        self._assigned_routes = []


    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def max_range(self):
        return self._max_range
    
    @property
    def status(self):
        return self._status
    @property
    def assigned_routes(self):
        return tuple(self._assigned_routes)
    
    def assign_route(self, route):
        self._assigned_routes.append(route)
        self._assigned_routes = sorted(self.assigned_routes, key=lambda route: route.department_time) #Sort assigned routes by department time
    
    def status_travelling(self):
        self._status = TruckStatus.TRAVELLING

    def status_free(self):
        self._status = TruckStatus.FREE

    def status_assigned(self):
        self._status = TruckStatus.ASSIGNED

    def remove_route(self, route):
        self._assigned_routes.remove(route)

    def __str__(self):
        return f'{self.name}-{self.id} Capacity({self.capacity}) Range({self.max_range})'
