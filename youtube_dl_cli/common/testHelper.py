__all__ = ('ShowTestDescription',
           )

from .consoleHelper import *
import unittest

from typing import Callable, Any


class ShowTestDescription(unittest.TestCase):
    def setUp(self) -> None:
        # print(self.__doc__)  # class doc
        # print(self._testMethodName)  # function name

        print_text('\n' + str(self), Fore.BLUE)
        document = self._testMethodDoc if self._testMethodDoc else 'No documents.'
        print(f"\t{text_color(document)}")  # function doc

    def shortDescription(self) -> None:
        return super().shortDescription()

    def tearDown(self) -> None:
        super().shortDescription()  # print('leave the function')


class CLITestsBase(ShowTestDescription):

    def __init__(self,
                 sub_cmd: str, cli_main: Callable[[list], Any],
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cli_main = cli_main
        self.cmd_list = [sub_cmd]
        self.__sub_cmd = sub_cmd
        self.start_run = self.decorator_run()

    def tearDown(self) -> None:
        self.cmd_list = [self.__sub_cmd]  # reset cmd_list

    def decorator_run(self):
        def wrap(para_list: list):
            self.cmd_list.extend(para_list)
            self.cmd_list = [str(_) for _ in self.cmd_list]  # .. important:: make sure all parameter is str for simulating the input from the command line
            print(f"Run command:{text_color(' '.join(self.cmd_list))}")
            return self.cli_main(self.cmd_list)
        return wrap
