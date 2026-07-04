def longest_consecutive_seq(nums: list[int]) -> int:

    num_set = set(nums)
    longest = 0

    for num in nums:

        if (num - 1) not in num_set:

            current_num = num
            current_len = 1

            while (current_num + 1) in num_set:
                current_num += 1
                current_len += 1

            longest = max(longest, current_len)

    return longest

nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_seq(nums)
print(result)