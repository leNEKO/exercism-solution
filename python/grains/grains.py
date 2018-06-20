def validate(func):
    def wrapper(i):
        if not (1 <= i <= 64):
            raise ValueError("1<=i<=64")
        return func(i)
    return wrapper


@validate
def on_square(i):
    return (2 ** (i - 1))


@validate
def total_after(i):
    return (2 ** i) - 1
