from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData
from models.constants.user_roles import UserRole


class LoginUserCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        super().__init__(params, app_data)

    def execute(self):
        role = self.params[0]
        if self.app_data.logged_user:
            return f'{str(self.app_data.logged_user).capitalize()} already logged in. Please log out first!'
        if role in [UserRole.EMPLOYEE, UserRole.SUPERVISOR, UserRole.MANAGER]:
            self.app_data.login(role)
            return f'{role.capitalize()} successfully logged in.'
        else:
            return 'Incorrect employee type.'
