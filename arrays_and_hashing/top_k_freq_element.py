from collections import defaultdict

def top_k_freq_elements(nums: list[int], k: int) -> list[int]:

    count = defaultdict(int)

    for num in nums:
        count[num] += 1

    freq = [[] for _ in range(len(nums) + 1)]

    for num, cnt in count.items():
        freq[cnt].append(num)

    result = []

    for bucket in reversed(freq):

        for num in bucket:
            result.append(num)

            if len(result) == k:
                return result

    return result





