
from core.app_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
from files.files_factory import FilesFactory

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
files_factory = FilesFactory(app_data)
engine = Engine(cmd_factory,files_factory)

engine.start()