from models.package import Package
from models.route import Route


class ModelsFactory:
    def __init__(self):
        self._package_id = 1
        self._route_id = 1

    def create_package(self, start_location: str, destination: str, weight: int, contact_info: str):
        package_id = self._package_id
        self._package_id += 1
        return Package(package_id, start_location, destination, weight, contact_info)

    def create_route(self, department_time, start_location: str, destination):
        route_id = self._route_id
        self._route_id += 1
        return Route(route_id, department_time, start_location, destination)

