from commands.assign_package import AssignPackageCommand
from commands.create_package import CreatePackageCommand
from commands.create_route import CreateRouteCommand
from commands.assign_truck import AssignTruck
from commands.login_user import LoginUserCommand
from commands.logout_user import LogOutUserCommand
from commands.view_package import ViewPackageCommand
from commands.view_routes_in_progress import ViewRoutesInProgressCommand
from commands.view_unassigned_packages import ViewUnassignedPackagesCommand
from commands.add_days import AddDaysCommand
from commands.view_routes import ViewRoutesCommand
from core.app_data import ApplicationData
from core.models_factory import ModelsFactory


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data
        self._models_factory = ModelsFactory()

    def create(self, input_line: str):
        cmd, *params = input_line.split()

        if cmd.lower() == "createpackage":
            return CreatePackageCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "createroute":
            return CreateRouteCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "assignpackage":
            return AssignPackageCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "assigntruck":
            return AssignTruck(params, self._app_data)
        if cmd.lower() == "viewunassignedpackages":
            return ViewUnassignedPackagesCommand(params, self._app_data)
        if cmd.lower() == "adddays":
            return AddDaysCommand(params, self._app_data)
        if cmd.lower() == "viewroutes":
            return ViewRoutesCommand(params, self._app_data)
        if cmd.lower() == "viewpackage":
            return ViewPackageCommand(params, self._app_data)
        if cmd.lower() == "loginuser":
            return LoginUserCommand(params, self._app_data)
        if cmd.lower() == "logoutuser":
            return LogOutUserCommand(params, self._app_data)
        if cmd.lower() == "viewroutesinprogress":
            return ViewRoutesInProgressCommand(params, self._app_data)
        raise ValueError(f'Invalid command name: {cmd}!')



