class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums) - 2, -1, -2):
            j = random.randint(0, i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums


def _driver():
    nums = [2, 5, 1, 3, 4, 7]  # Define the 'nums' array
    solution = Solution(nums)  # Pass 'nums' to the Solution constructor
    ret = solution.shuffle()
    print(ret)
    ret = solution.reset()
    print(ret)

if __name__ == "__main__":
    _driver()
