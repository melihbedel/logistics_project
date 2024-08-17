from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData


class LogOutUserCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        super().__init__(params, app_data)

    def execute(self):
        user = self.params[0]
        if not self.app_data.logged_user:
            return f'{user.capitalize()} not logged in and cannot log them out.'
        elif user == self.app_data.logged_user:
            self.app_data.logout()
            return f'{user.capitalize()} successfully logged out.'
        else:
            return f'{user} is not logged in. Currently {self.app_data.logged_user} is logged in.'