def unique_elements(nested_list):
    unique_set = set()
    def flatten_list(lst):
        for item in lst:
            if isinstance(item, list):

                flatten_list(item)
            else:                
                unique_set.add(item)
    flatten_list(nested_list)
    return sorted(unique_set)

list_a = [
    1,2,3 , [4,3,1], 5 , [6, [7,[10], 8,[9,2,3]]]]


print(unique_elements(list_a)) 

