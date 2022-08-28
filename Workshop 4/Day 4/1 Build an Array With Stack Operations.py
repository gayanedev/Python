""" Return the stack operations needed to build target array """
def build_array(target, n):
    output = []
    index = 0

    for i in range(1, n + 1):
        if target[index] == i:
            output.append('Push')
            index += 1
        else:
            output.append('Push')
            output.append('Pop')

        if index == len(target):
            break
    return output


list_target = list(map(int, input('Enter elements: ').split()))
num = int(input('Enter number: '))

print(build_array(list_target, num))