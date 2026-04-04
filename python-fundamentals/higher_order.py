def apply_twice(func, value):
    """Applies the given function twice to the value using lambda function"""
    return func(func(value))

def compose(f, g):
    """returns a new function that applies g then f"""
    def composed_function(x):
        return f(g(x))
    return composed_function

def make_multiplier(n):
    """returns a function that multiplies its input by n"""
    def multiplier(x):
        return x * n
    return multiplier

def my_map(func, items):
    """Reimplements python's map"""
    result = []
    for item in items:
        result.append(func(item))
    return result

def my_filter(func, items):
    """Reimplements python's filter"""
    result = []
    for item in items:
        if func(item):
            result.append(item)
    return result

def main():
    # Example usage of the functions
    print(apply_twice(lambda x: x * 2, 3))  # Output: 12
    add_one = lambda x: x + 1
    double_then_add_one = compose(add_one, lambda x: x * 2)
    print(double_then_add_one(3))  # Output: 7
    times_three = make_multiplier(3)
    print(times_three(5))  # Output: 15
    print(my_map(lambda x: x * 2, [1, 2, 3]))  # Output: [2, 4, 6]
    print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # Output: [2, 4]
    
if __name__ == "__main__":    main()