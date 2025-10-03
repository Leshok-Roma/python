def type_check(*types): 
    def decorator(func):
        def wrapper(*args , **kwargs ): 
            for arg, type in zip(args, types):
                if not isinstance(arg, type):
                    raise TypeError('Несоответсвие типов')
            return func(*args, **kwargs)
        return wrapper
    return decorator 
#type_check = lambda *t: lambda f: lambda *a: len(a) == len(t) and all(type(x) == y for x, y in zip(a, t)) and f(*a) or exec('raise TypeError("Несоответствие типов")')

@type_check(int ,int)
def test_func(a, b): 
    return a + b

print(test_func(1,2))
