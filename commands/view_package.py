from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData


class ViewPackageCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        super().__init__(params, app_data)


    def execute(self):
        super().execute()
        package_id = int(self.params[0])
        package = self.app_data.find_package_by_id(package_id)
        if package:
            return '\n'.join(
                ['----------'] +
                ['Package details'] +
                [f'{package}'] +
                [f'Package status: {package.status.value}'] +
                [f'Detailed information sent to {package.contact_info}'] +
                ['----------'])
        return f"Package #{package_id} not found in the system."
    def requires_login(self):
        return True