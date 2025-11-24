def find_unique(items):
    if not isinstance(items, list):
        raise TypeError("should be list")

    unique = []
    for item in items:
        if items.count(item) == 1:
            unique.append(item)
    return unique
