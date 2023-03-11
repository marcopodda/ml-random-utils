"""General-purpose decorators."""

import time
from typing import Callable, Iterable
from functools import wraps
from multiprocessing import cpu_count

from joblib import Parallel, delayed


def parallelize(**kwargs) -> Callable:
    """
    Returns a function that takes an iterable and calls it with
    each item of the iterable in parallel using joblib. If `item`
    is not a single element (e.g. a tuple or a list), it is the
    responsibility of the function to which the decorator is
    applied to unpack it. If not provided, kwarg argument `n_jobs`
    will be set to the number of available CPUs minus 2.

    Arguments:
        **kwargs: arguments to pass to joblib.Parallel
    Returns:
        a function that can be called with an iterable as argument.
        Each function call will be processed in parallel using joblib.
    """
    kwargs["n_jobs"] = kwargs.get("n_jobs", max(cpu_count() - 2, 1))

    def wrapper(func: Callable) -> Callable:

        @wraps(func)
        def inner(items: Iterable) -> Iterable | None:
            executor = Parallel(**kwargs)
            job = delayed(func)
            return executor(job(item) for item in items)
        return inner

    return wrapper


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
