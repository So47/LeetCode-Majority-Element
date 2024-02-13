class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums_counter = Counter(nums)
        # return nums_counter.most_common()[0][0]
        nums.sort()
        return nums[len(nums)//2]
        
