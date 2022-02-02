def lengthOfLIS(nums: [int]) -> int:
    def lis(nums: [int], index=0, d=0, memo={}):

        if index in memo:
            return memo[index]

        if nums:
            sequences = []

            for i, num in enumerate(nums):
                tail = [n for n in nums[i + 1:] if n > num]
                sequences.append(lis(tail, index + i + 1, d + 1))

            memo[index] = max(sequences)
            return memo[index]

        return d

    print(lis([3,5,6,2,5,4,19,5,6,7,12]))


lengthOfLIS([])