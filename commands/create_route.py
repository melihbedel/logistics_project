from commands.base.base_command import BaseCommand
from core.app_data import ApplicationData
from core.models_factory import ModelsFactory
from datetime import datetime


class CreateRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        super().execute()
        year, month, day, hour, minutes, start_location, *destination = self.params
        try:
            year = int(year)
            month = int(month)
            day = int(day)
            hour = int(hour)
            minutes = int(minutes)
        except:
            raise ValueError('Date must be in the format Y M D H m, and ALL must be integers')
        if year < 2022:
            raise ValueError('Year should not be in the past')
        if month < 1 or month > 12:
            raise ValueError('Month should be between 1 and 12')
        if day < 1 or day > 31:
            raise ValueError('Day should be between 1 and 31')
        if not isinstance(hour, int) or hour < 0 or hour > 24:
            raise ValueError('Hour should be between 0 and 24')
        if not isinstance(minutes, int) or minutes < 0 or minutes > 60:
            raise ValueError('Minutes should be between 0 and 60')

        department_time = datetime(int(year), int(
            month), int(day), int(hour), int(minutes))
        if department_time < self.app_data._current_time:
            raise ValueError(
                'Route cannot be created to depart before the current time')
        route = self.models_factory.create_route(
            department_time, start_location, tuple(destination))
        self._app_data.add_route(route)
        return f'Route #{route.id} created!'

    def requires_login(self):
        return True