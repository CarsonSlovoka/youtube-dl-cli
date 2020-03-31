__all__ = ('Fore', 'Back', 'AlignText',  # class

           'print_text', 'text_color'  # function
           )
import colorama
from colorama.ansi import AnsiFore
from colorama import Fore, Back
colorama.init(autoreset=True)


def highlight_print(msg: str, fore_color: AnsiFore = Fore.RED) -> None:
    print(Back.LIGHTYELLOW_EX + fore_color + msg)


class AlignText:
    __slots__ = ['align_list']

    def __init__(self, align_list: list):
        self.align_list = align_list

    def __call__(self, text_list: list):
        if len(text_list) != len(self.align_list):
            raise AttributeError
        return ' '.join(f'{txt:{flag}{int_align}}' for txt, (int_align, flag) in zip(text_list, self.align_list))


def text_color(msg, fore_color: Fore = Fore.GREEN, back_color: Back = ""):
    if not isinstance(msg, str):
        msg = str(msg)
    return back_color + fore_color + msg + Fore.RESET


def print_text(msg, fore_color: Fore, back_color: Back = ""):
    """
    print_text(class_name, Fore.BLUE, back_color=Back.YELLOW)
    """
    if not isinstance(msg, str):
        msg = str(msg)
    print(text_color(msg, fore_color, back_color))
