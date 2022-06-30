""" Split a string into a list of strings """
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

# the string splits at this specified separator
# input string separator
string_sep = str(input('Enter substring: '))

# split the string into maximum number of times
max_split = input('Enter maxsplit: ') or None

print(split(string, string_sep, max_split))