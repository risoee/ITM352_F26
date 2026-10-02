test_cases = [
    [],
    ["a", "b", "c", "d"],
    ["a", "b", "c", "d", "e"],
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
]

for test_list in test_cases:
    if len(test_list) < 5:
        print("Fewer than 5 elements")
    elif len(test_list) <= 10:
        print("Between 5 and 10 elements")
    else:
        print("More than 10 elements")