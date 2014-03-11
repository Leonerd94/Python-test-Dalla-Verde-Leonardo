# ex 2

def add_dict(dict_1, dict_2):
    return (dict_1.items()+dict_2.items())


dic1 = {
        'leonardo':'room1',
        'giacomo':'room2',
        'elia':'room3'
}

dic2 = {
        'elia':'room4',
        'jack':'room5',
        'stefano':'room6'
}

print add_dict(dic1, dic2)

