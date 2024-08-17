from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData


class ViewUnassignedPackagesCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 0)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        packages = self.app_data.view_unassigned_packages()
        if self.app_data.logged_user == 'employee':
            return 'Employee cannot see this information.'
        result = '----------\n' \
                 'Packages waiting to be assigned:\n'
        result_list = []
        counter = 1
        for package in packages:
            result_list.append(f"{counter}. {package}")
            counter += 1
        result += '\n'.join(result_list)
        return result


    def requires_login(self):
        return True