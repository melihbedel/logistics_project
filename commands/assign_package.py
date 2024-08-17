from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData
from core.models_factory import ModelsFactory


class AssignPackageCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        validate_params_count(params, 1)
        super().__init__(params, app_data)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        super().execute()
        package_id_to_assign = int(self.params[0])
        package_to_assign = self.app_data.find_package_by_id(package_id_to_assign)
        route = self.app_data.find_route_to_assign_package(package_to_assign)
        if route:
            package_to_assign.advance_status_to_assigned()
            route._packages.append(package_to_assign)
            return f"Package #{package_id_to_assign} assigned to route #{route.id}."

        return 'No route found for this package'

    def requires_login(self):
        return True


