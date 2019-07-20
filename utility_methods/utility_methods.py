import functools
import time

def dtu_method(func):
    """
    DTU method decorator. Sleeps for 2 seconds before and after calling any methods that interact with Instagram.
    Args:
        func:function: Function to wrap
    Returns:
        wrapper:function: Wrapper function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        func(*args, **kwargs)
        time.sleep(2)

    return wrapper
