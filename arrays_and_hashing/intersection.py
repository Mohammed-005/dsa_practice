def intersection(nums1: list[int], nums2: list[int]) -> list[int]:

    #nums1_set = set(nums1)
    #nums2_set = set(nums2)
    #return list(nums1_set.intersection(nums2_set))

    nums1_set = set(nums1)
    result_set = set()

    for num in nums2:
        if num in nums1_set:
            result_set.add(num)

    return list(result_set)

print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))

