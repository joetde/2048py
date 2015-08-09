
from time import time

from helpers.logger import log

def with_time(func):
  ''' Helper decorator for timing function. '''
  def wrapper(*args, **kwargs):
    start = time() * 1000
    ret = func(*args, **kwargs)
    end = time() * 1000
    time_spent = int(end - start)
    # note: doesn't show class name for methods
    log.debug('<%s.%s> Time spent: %sms', func.__module__, func.__name__, time_spent)
    return ret
  return wrapper

def with_count(func):
  ''' Helper decorator for counted instructions. '''
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  return wrapper
