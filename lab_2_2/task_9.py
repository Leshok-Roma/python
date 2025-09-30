def type_check(*types): 
    def decorator(func):
        def wrapper(*args , **kwargs ): 
            for arg, type in zip(args, types):
                if not isinstance(arg, type):
                    raise TypeError('Несоответсвие типов')
            return func(*args, **kwargs)
        return wrapper
    return decorator 


@type_check(int , int )
def test_func(a, b ): 
    return a  + b

print(test_func(1,2))
print(test_func("1" , "2"))