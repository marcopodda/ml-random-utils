from typing import Iterable
from functools import wraps

from typing import Iterable
from multiprocessing import cpu_count
from joblib import Parallel, delayed


def parallelize(**kwargs):
    if "n_jobs" not in kwargs:
        kwargs["n_jobs"] = max(cpu_count() - 2, 1)

    def wrapper(func):

        @wraps(func)
        def inner(iterable: Iterable) -> Iterable | None:
            executor = Parallel(**kwargs)
            job = delayed(func)
            return executor(job(item) for item in iterable)
        return inner

    return wrapper
