from functools import wraps
def tipe_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        rezult = func(*args, **kwargs)
        for i in args:
            print(f'Call for: {func.__name__}')
            print(i, ':', type(i), end="\n ")
        for key, value in kwargs.items():
            print("'{0}' = {1}:".format(key, value), type(value), end=", ")

        print("\n ", 'Rezult: ', rezult, 'type: ', type(rezult))
        return
    return wrapper

@tipe_logger
def calc_cube(x):
    return x **3

@tipe_logger
def rendenr_input(*args, **kwargs):
    return 1




