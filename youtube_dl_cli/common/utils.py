from contextlib import contextmanager
from pathlib import Path
from os import remove
from typing import Callable


@contextmanager
def after_end(cb_fun: Callable):
    """
    with after_end(cb_fun) as cb_fun:
        ...
    """
    try:
        yield cb_fun
    finally:
        cb_fun()
