def sort_dict_by_values(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1]))

example_dict = {'a': 3, 'b': 1, 'c': 2}
print(sort_dict_by_values(example_dict))
