from core.app_data import ApplicationData


class BaseCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    @property
    def params(self):
        return tuple(self._params)

    @property
    def app_data(self):
        return self._app_data

    def execute(self):
        if self.requires_login() and not self.app_data.has_logged_in_user():
            raise ValueError('No user is logged in. Please login first.')


    def requires_login(self):
        raise NotImplementedError('Override in derived class')