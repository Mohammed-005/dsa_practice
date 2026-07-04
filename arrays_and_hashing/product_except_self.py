def product_except_self_2(nums: list[int]) -> list[int]:

    result = [1] * len(nums)

    left_total = 1
    for i in range(len(nums)):
        result[i] = left_total
        left_total *= nums[i]

    right_total = 1
    for i in reversed(range(len(nums))):
        result[i] *= right_total
        right_total *= nums[i]

    return result