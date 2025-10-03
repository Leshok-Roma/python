def flatten_list(lst):
    def step(index):
        if index >= len(lst):
            return
        if isinstance(lst[  index], list):
            current = lst.pop(index)
            lst[index:index] = current
            helper(index)
        else:
            helper(index + 1)
    step(0)


lst = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(lst)

