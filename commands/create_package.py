from commands.base.base_command import BaseCommand
from core.app_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.validators import validate_params_count
from models.constants.locations import Locations


class CreatePackageCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        validate_params_count(params, 4)
        super().__init__(params, app_data)
        self._models_factory = models_factory
        # logged_user = self._app_data.logged_in_user

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        super().execute()
        start_location = self.params[0]
        if start_location not in [loc.value for loc in Locations]:
            raise ValueError(f'The location is invalid.')
        destination = self.params[1]
        if destination not in [loc.value for loc in Locations]:
            raise ValueError(f'The location is invalid.')
        weight = int(self.params[2])
        if weight < 0:
            raise ValueError('The weight of the package cannot be negative')
        contact_info = self.params[3]
        package = self.models_factory.create_package(start_location, destination, weight, contact_info)
        self.app_data.add_package(package)
        self.app_data.add_package_to_location_storage(start_location, package)
        return f"Package #{package.id} created!"

    def requires_login(self):
        return True