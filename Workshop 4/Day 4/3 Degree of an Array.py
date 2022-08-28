""" Find the smallest possible length of a subArray of nums, that has the same degree as nums array """
def find_shortest_sub_array(nums):
    counts = {}
    starts = {}
    ends = {}

    for i in range(len(nums)):
        if nums[i] not in counts:
            counts[nums[i]] = 1
        else:
            counts[nums[i]] += 1

    degree = max(counts.values())

    for i in range(len(nums)):
        if nums[i] not in starts:
            starts[nums[i]] = i

        ends[nums[i]] = i

    return min(ends[num] - starts[num] + 1 for num in counts.keys() if counts[num] == degree)


num_lst = list(map(int, input('Enter list elements: ').split()))

print(find_shortest_sub_array(num_lst))