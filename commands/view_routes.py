from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData


class ViewRoutesCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 0)
        super().__init__(params, app_data)

    def execute(self):
        super().execute()
        output = '----------' \
                 '\nAll routes in the system:'
        for route in self._app_data.routes:
            output += '\n----------'
            output += '\n' + str(route)
        return output

    def requires_login(self):
        return True