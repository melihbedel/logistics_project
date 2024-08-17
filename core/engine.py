
from core.command_factory import CommandFactory
from files.files_factory import FilesFactory


class Engine:
    def __init__(self, cmd_factory: CommandFactory, files_factory: FilesFactory):
        self._command_factory = cmd_factory
        self._files_factory = files_factory
        self.read_from_input_log_file()
        self.update_app_data()

    def start(self):
        output: list[str] = []
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break
                self._files_factory.append_input_log(input_line)

                command = self._command_factory.create(input_line).execute()
                output.append(command)
                self._files_factory.append_event_log(command)
            except ValueError as err:
                output.append(err.args[0])
                self._files_factory.append_event_log(err.args[0])

        print('\n'.join(output))

    def read_from_input_log_file(self):
        self._files_factory.clear_event_log()
        input_lines = self._files_factory.read_input_log()

        for input_line in input_lines:
            try:
                if input_line.lower() == 'end':
                    break
                command = self._command_factory.create(input_line).execute()
                self._files_factory.append_event_log(command)
            except ValueError as err:
                self._files_factory.append_event_log(err.args[0])

    def update_app_data(self):
        self._files_factory.update_time()
        self._files_factory._app_data.update_routes()
