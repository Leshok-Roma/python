def cashe(func):
    cashe_dictionary = {} 
    def wrapper(*args, **kwargs):
        key = (args , tuple(sorted(kwargs.items())))
        if key in cashe_dictionary: 
            return cashe_dictionary[key]
        else :
            result = func(*args, **kwargs)
            cashe_dictionary[key] = result
        return result
    return wrapper

@cashe
def test_sum(a,b): 
    return(a+b)

res = test_sum(1 ,2 )
print(res)