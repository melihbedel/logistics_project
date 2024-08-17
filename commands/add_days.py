from commands.base.base_command import BaseCommand
from commands.validators import validate_params_count
from core.app_data import ApplicationData


class AddDaysCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        validate_params_count(params, 2)
        super().__init__(params, app_data)


    def execute(self):
        days, hours = self.params
        self._app_data.add_days_to_now(days, hours)
        return f'{days} days and {hours} hours added! \nCurrent time: {self.app_data.current_time.strftime("%Y/%m/%d, %H:%M")}'


