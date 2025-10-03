def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(value, dict):
                merge_dicts(dict1[key], value)
            elif isinstance(dict1[key], list) and isinstance(value, list):
                dict1[key].extend(value)    
            
            elif isinstance(dict1[key], set) and isinstance(value, set):
                dict1[key].update(value)
            
            elif isinstance(dict1[key], tuple) and isinstance(value, tuple):
                dict1[key] = dict1[key] + value
            else:
                dict1[key] = value
        else:
            dict1[key] = value
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(dict_a)  
