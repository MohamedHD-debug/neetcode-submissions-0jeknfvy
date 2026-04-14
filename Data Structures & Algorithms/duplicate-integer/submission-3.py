class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_nums_set = set(nums)    
        return (len(list_nums_set) != len(nums))