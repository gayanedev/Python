""" Replace the old substring with the new substring """
def replace(source, old, new, count=None):
    n_count = 0

    if (count is None) or int(count) > source.count(old):
        count = source.count(old)

    while n_count < int(count):
        low_index = source.find(old)
        high_index = low_index + len(old)
        source = source[:low_index] + new + source[high_index:]
        n_count += 1
    return source


# input string
string = str(input('Enter string: '))

# input old substring that we want to replace
old_sub = str(input('Enter old substring: '))

# input new substring which would replace the old substring
new_sub = str(input('Enter new substring: '))

# input number of times that we want to replace the old substring with the new substring
count_rep = input('Enter count: ') or None

print(replace(string, old_sub, new_sub, count_rep))