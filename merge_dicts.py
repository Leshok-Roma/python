def merge_dicts(dict1, dict2):

    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Should be two dictionaries")
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

    return dict1
