class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        good_pairs = 0
        for num in nums:
            good_pairs += counts[num]
            counts[num] += 1
        return good_pairs