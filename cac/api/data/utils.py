

def simple_time_cache(max_age, maxsize=10, typed=False):
    def _time_call(func):
        @functools.lru_cache(maxsize=maxsize, typed=typed)
        def _run(*args, _time, **kwargs):
            return func(*args, **kwargs)
        