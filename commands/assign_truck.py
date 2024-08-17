from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData
from models.constants.truck_status import TruckStatus


class AssignTruck(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        validate_params_count(params, 1)
        # parameter: Route ID
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        route_id = int(self.params[0])
        route = self.app_data.find_route_by_id(route_id)
        if route:
            truck = self.app_data.assign_truck_to_route(route)
            if truck:
                truck._assigned_routes.append(route)
                truck.status_assigned()
                return f'Truck #{truck.id} assigned to route #{route.id}.'
            return 'No truck found for this route'
        return f'Route #{route_id} not found in the system.'
        
        #When truck is available and route exists, assign the truck to the route

    def requires_login(self):
        return True