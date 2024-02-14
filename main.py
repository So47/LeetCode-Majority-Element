class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Time Complexity: O(n) due to the counting operation, with a practical performance near O(n) for finding the most common element due to optimizations, though theoretically it could approach O(n log n) in the worst case.
        ## Space Complexity: O(k), where k is the number of unique elements in the nums array, for storing the counts of each element.
        
        # nums_counter = Counter(nums) # O(n)
        # return nums_counter.most_common()[0][0] # O(n log n)

        ## Time Complexity: O(nlogn), dominated by the sorting operation.
        ## Space Complexity: O(n) in the worst case due to the sorting algorithm, although for practical purposes, especially with smaller arrays or arrays that are partially sorted, the auxiliary space used might be less.

        # nums.sort()
        # return nums[len(nums)//2]

        # Using Boyer-Moore Voting Algorithm. This algorithm has a linear time complexity of O(n) and constant space complexity of O(1),
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate 

        
