

############ template for decorators ######################"
# def decorator(func):
#     @functools.wraps(func) # to keep identity of the function inputted
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
##############################################################


import functools # for the wraps decorator to keep track of identity of the function input


# decorator temps passé dans une fonction
import os
from logger import *

## configuration logging
# cleaning message log file first
file_name_log = 'timer.log'
if os.path.exists(file_name_log):
    os.remove(file_name_log)
# config of logging
setup_logger('log_timer', file_name_log, logging.DEBUG)
log_timer = logging.getLogger('log_timer')

import time
def timer(func):
    # """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        log_timer.info(f"Finished {func.__qualname__!r} in {run_time:.4f} secs")
        # print(f"Finished {func.__qualname__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

