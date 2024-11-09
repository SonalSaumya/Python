import logging
def simple_logger(func):
    
    logging.basicConfig(filename='test.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    def wrapper (*args,**kwargs):

        print(f"Starting {func.__name__}")
        result = func(*args,**kwargs)
        print(f"Finished {func.__name__}")
        return result

    return  wrapper

@simple_logger
def greet(name):
    print(f"hello, {name}")


greet("Sonal")


# import logging
# def log_to_file(log_file, log_level=logging.INFO):
#
#     logging.basicConfig(
#         filename=log_file,
#         level=log_level,
#         format='%(asctime)s - %(levelname)s - %(message)s'
#     )
#
#     def decorator(func):
#          def wrapper(*args, **kwargs):
#              logging.log(log_level, f"Starting{func.__name__}...")
#              result = func(*args, **kwargs)
#              logging.log(log_level, f"Finished {func.__name__}.")
#              return result
#          return wrapper



# def pname(func):
#     def wrapper(*args,**kwargs):
#         print(func.__name__)
#     return wrapper()
#
# @pname
# def my_function():
#     pass
#
# my_function












