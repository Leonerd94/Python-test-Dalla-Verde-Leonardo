# ex 1


def dict_values_ascending(d):
    return sorted(d.items(), key=lambda x: x[1])




dix = {
    'leonardo':'desk1',
    'giulio':'desk2',
    'mike':'room3',
    'jonny':'desk3'
}

print dict_values_ascending(dix)