""" Split the string by specified separator """
def split(source, sep, count=None):
    res = []
    n_count = 0

    if (count is None) or int(count) > source.count(sep):
        count = source.count(sep)

    while n_count < int(count):
        low_index = source.find(sep)
        high_index = low_index + len(sep)
        res.append(source[:low_index])
        source = source[high_index:]
        n_count += 1
    res.append(source)
    return res


# input string
string = str(input('Enter string: '))

# input separator
string_sep = str(input('Enter separator: '))

# input number or times that we want to split
count_split = input('Enter count: ') or None

print(split(string, string_sep, count_split))