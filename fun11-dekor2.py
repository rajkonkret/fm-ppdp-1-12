def uppercase_decorator(funk):
    def wrapper():
        result = funk()
        return result.upper()

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World"


print(greeting())
