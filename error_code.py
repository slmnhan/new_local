def absolute_value_wrong(x):
    if x < 0:
        return -x
    if x > 0:
        return x
    return "this is dead code"
    
print(absolute_value_wrong(-10))