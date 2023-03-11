"""General-purpose decorators."""

import time
from typing import Callable
from functools import wraps


def timeit(func: Callable) -> Callable:
    """
    Prints the time elapsed by any function.

    Arguments:
        func (Callable): any function

    Returns:
        the same function, but prints its running time once executed.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        start_time = time.time()
        return_value = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Running time of {func.__name__}: {elapsed} (s)")
        return return_value

    return wrapper


def dedup(func: Callable[..., list]) -> Callable[..., list]:
    """
    Eliminates duplicates from a returned list.

    Arguments:
        func (Callable): any function that returns a list.

    Returns:
        a function that returns a list without duplicates.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> list:
        result_list = func(*args, **kwargs)
        return list(set(result_list))

    return wrapper
