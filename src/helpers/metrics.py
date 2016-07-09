from time import time

from helpers.logger import log


def with_time(func):
    """ Helper decorator for timing function. """

    def wrapper(*args, **kwargs):
        start = time() * 1000
        ret = func(*args, **kwargs)
        end = time() * 1000
        time_spent = int(end - start)
        # note: doesn't show class name for methods
        log.debug('<%s.%s> Time spent: %sms', func.__module__, func.__name__, time_spent)
        return ret

    return wrapper


COUNTER_DICT = {}


def with_count(func_weight=1):
    """ Helper decorator for counted instructions. """

    def wrapper_counter(func):
        def wrapper(*args, **kwargs):
            full_name = func.__module__ + '.' + func.__name__
            if full_name in COUNTER_DICT:
                COUNTER_DICT[full_name] += func_weight
            else:
                COUNTER_DICT[full_name] = func_weight
            return func(*args, **kwargs)

        return wrapper

    return wrapper_counter
