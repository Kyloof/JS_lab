import logging
import time
from typing import Callable
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

def log(log_level):
    def decorator(param):
        # Class
        if isinstance(param, type):
            original_new = param.__new__

            def __new__(cls, *args, **kwargs):
                logger = logging.getLogger(param.__module__ + '.' + param.__name__)
                logger.log(log_level, f'Object {param.__name__} has been created.')

                instance = original_new(cls)
                return instance

            param.__new__ = __new__
            return param
        # Function
        elif isinstance(param, Callable):

            def wrapper(*args, **kwargs):
                logger = logging.getLogger(param.__module__)

                start = time.perf_counter()

                logger.log(log_level, f'Function {param.__name__} called with args = {args} and kwargs = {kwargs}.')
                logger.log(log_level, f'Function {param.__name__} has been called on {datetime.now()}')
                result = param(*args, **kwargs)

                end = time.perf_counter()
                logger.log(log_level, f'Function {param.__name__} took {end - start:.6f} seconds to execute.')

                logger.log(log_level, f'Function {param.__name__} returned {result}.')
                return result
            return wrapper
        raise TypeError()
    return decorator


@log(logging.DEBUG)
class Osoba:
    def __init__(self, wiek):
        self.wiek = wiek

@log(logging.CRITICAL)
def ret_1(o:int):
    return o

a = Osoba(2)

ret_1(1)