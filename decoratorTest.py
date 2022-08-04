import time

def  decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f'duration {duration}')
    return wrapper

@decorator
def func():
    print('function')


def repetion_decorator(repetitions):
    def decorator(func):
        def wrapper():
            for r in range(repetitions):
                func()
        return wrapper
    return decorator


@repetion_decorator(5)
def func2():
    print('function')

func()
func2()