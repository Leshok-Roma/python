import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):

            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            args_str = ", ".join([str(arg) for arg in args])
            kwargs_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])            
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))          
            with open(filename, 'a') as f:
                f.write(f"{time_now} - {func.__name__}({all_args})\n")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("test.txt")
def test(a , b = 10 ):
    return  a + b

test (1, 12 )
