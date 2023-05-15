def take(items, n = 1):
    if n > len(items):
        return items
    return items[:n]
    
print(take([1, 2, 3], 2))