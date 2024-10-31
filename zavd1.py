original_tuple = (3, 7, 2, 9, 5, 1, 4, 3.14, 2.5, 1.715, 0.5)

integers = [x for x in original_tuple if isinstance(x, int)]
floats = [x for x in original_tuple if isinstance(x, float)]

max_integer = max(integers)
max_float = max(floats)

CF = (max_integer, max_float)

print("Кортеж CF:", CF)