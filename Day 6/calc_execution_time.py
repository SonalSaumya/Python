import time
from functools import wraps
def log_func_name(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args,**kwargs)
    return wrapper

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name___}):  {execution_time:.4f} seconds")
        return result
    return wrapper

def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = example_function(1000000)

