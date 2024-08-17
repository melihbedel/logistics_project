from models.constants.package_status import PackageStatus
from models.constants.truck_status import TruckStatus
from models.package import Package
from models.route import Route
from models.truck import Truck
from models.location import Location
from models.constants.locations import Locations
from models.constants.route_status import RouteStatus
from models.constants.package_status import PackageStatus
from datetime import datetime, timedelta


class ApplicationData:
    def __init__(self):
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks: list[Truck] = []
        self.assign_trucks_instancing()
        self._locations: list[Location] = [Location(location.value) for location in Locations]
        # Set the initial time to the moment of instancing
        self._current_time: datetime = None
        self.logged_user = None

    @property
    def locations(self):
        return self._locations

    @property
    def packages(self):
        return tuple(self._packages)

    @property
    def routes(self):
        return tuple(self._routes)

    @property
    def trucks(self):
        return tuple(self._trucks)

    @property
    def current_time(self):
        return self._current_time

    def add_package(self, package: Package):
        self._packages.append(package)

    def add_package_to_location_storage(self, location, package):
        for loc in self.locations:
            if location == loc.name:
                loc.storage.append(package)
                break

    def add_route(self, route: Route):
        self._routes.append(route)

    def find_package_by_id(self, package_id):
        for p in self.packages:
            if p.id == package_id:
                return p

    def truck_has_space(self, package, route):
        route_kg = sum([package.weight for package in route.packages])
        if package.weight + route_kg <= route.truck.capacity:
            return True
        return False

    def find_route_to_assign_package(self, package: Package):
        route_found = False
        for route in self.routes:
            if package.start_location == route.start_location and package.destination in route.destination:
                if route.truck and self.truck_has_space(package, route):
                    route_found = True
                    break
                route_found = True
                break
            elif package.start_location in route.destination and package.destination in route.destination:
                if route.destination.index(package.start_location) < route.destination.index(package.destination):
                    if route.truck and self.truck_has_space(package, route):
                        route_found = True
                    else:
                        route_found = False
                        break
                route_found = True
                break
        if route_found:
            return route
        return False

    def find_truck_by_id(self, id):
        for truck in self.trucks:
            if truck.id == id:
                return truck

    def find_route_by_id(self, id):
        for route in self.routes:
            if id == route.id:
                return route

    def view_unassigned_packages(self):
        unassigned_packages = []
        for package in self.packages:
            if package.status == PackageStatus.PENDING:
                unassigned_packages.append(package)
        return unassigned_packages

    def add_days_to_now(self, days, hours):
        self._current_time += timedelta(int(days), 0, 0, 0, 0, int(hours))
        self.update_routes()

    def update_routes(self):
        for route in self.routes:
            truck = route.truck
            if truck is not None:
                if self._current_time > route.department_time and self._current_time < route.arrival_time:
                    route.status = RouteStatus.DEPARTED
                    for loc, time in route.final_route.items():
                        if self._current_time >= time:
                            route.current_location = loc
                            self.check_for_delivered_package(route, loc)
                    for pack in route.packages:
                        pack.advance_status_to_on_track()
                    truck.status_travelling()
                if self._current_time >= route.arrival_time:
                    route.status = RouteStatus.COMPLETED
                    route.current_location = list(route.final_route.keys())[-1]
                    self.check_for_delivered_package(route, route.current_location)
                    # for pack in route.packages:
                    #     pack.advance_status_to_delivered()
                    truck.status_free()
                    truck.remove_route(route)
                    route._truck = None

    def login(self, user: str):
        self.logged_user = user

    def logout(self):
        self.logged_user = None

    def has_logged_in_user(self):
        if self.logged_user:
            return True
        return False

    def assign_truck_to_route(self, route:Route):
        route_km = route.distance
        weight = sum([package.weight for package in route._packages])
        for truck in self._trucks:
            if truck.status == TruckStatus.FREE and route_km <= truck.max_range and weight <= truck.capacity:
                route.truck = truck
                truck.assign_route(route)
                return truck
        for truck in self._trucks:
            if truck.status == TruckStatus.ASSIGNED:
                if truck.max_range <= route_km and truck.capacity <= weight:
                    if route.arrival_time < truck.assigned_routes[0].department_time:
                        route.truck = truck
                        truck.assign_route(route) 
                        return truck
                    for i in range(1, len(truck.assigned_routes)):
                        if route.department_time > truck.assigned_routes[i-1].arrival_time and route.arrival_time < truck.assigned_routes[i].department_time:
                            route.truck = truck
                            truck.assign_route(route)
                            return truck
                    if route.department_time > truck.assigned_routes[-1].arrival_time:
                        route.truck = truck
                        truck.assign_route(route)
                        return truck

    def assign_trucks_instancing(self):
        [self._trucks.append(Truck(id, 'Scania', 42000, 8000))
         for id in [i for i in range(1001, 1011)]]
        [self._trucks.append(Truck(id, 'Man', 37000, 10000))
         for id in [i for i in range(1011, 1026)]]
        [self._trucks.append(Truck(id, 'Actros', 26000, 13000))
         for id in [i for i in range(1026, 1041)]]


    def check_for_delivered_package(self, route, location):
        for package in route.packages:
            if location == package.destination:
                package.advance_status_to_delivered()
                route._packages.remove(package)


    def routes_in_progress(self):
        routes = [route for route in self.routes if route.status == RouteStatus.DEPARTED]
        return routes
