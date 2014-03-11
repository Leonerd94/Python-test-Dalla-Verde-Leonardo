# ex 3

def count_lines(name):
    in_f = open(name, 'rb')
    #count
    i = 0
    for line in in_f:
        i = i + 1
    return i


print count_lines('words.txt')