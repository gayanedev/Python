""" Find the index of the first occurrence of needle in haystack """
def str_str(haystack, needle):
    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        if haystack[i:m + i] == needle:
            return i
    return -1


# input string
hay_str = str(input("Enter the haystack string: "))

# input string
need_str = str(input("Enter the needle string: "))

print(str_str(hay_str, need_str))