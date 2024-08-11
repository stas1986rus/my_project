from functools import wraps


def log(filename=""):
    """Декоратор принимает необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль)"""

    def my_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as errors:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {errors.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {errors.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator


@log(filename="log.txt")
def my_function(x, y):
    return x + y


# print(my_function(3, 7))
print(my_function("2", 3))
