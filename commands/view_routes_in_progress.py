from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData


class ViewRoutesInProgressCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 0)
        super().__init__(params, app_data)


    def execute(self):
        super().execute()
        routes = self.app_data.routes_in_progress()
        if not self.app_data.logged_user == 'manager':
            return 'Only Manager can see this information'
        result = '---------\n' \
                 'Routes in progress:\n'
        result_list = ['----------']
        counter = 1
        for route in routes:
            result_list.append(f"{counter}. {route}")
            counter += 1
        result += '\n'.join(result_list)
        return result

    def requires_login(self):
        return True
