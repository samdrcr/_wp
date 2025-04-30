def dict_to_string(d):
    return ', '.join(f"{k}:{v}" for k, v in d.items())

print("Dict to string:", dict_to_string({'a': 1, 'b': 2}))

