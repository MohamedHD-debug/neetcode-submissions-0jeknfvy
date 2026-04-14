class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        nums_set = list(set(nums))

        counter = {}
        for i in nums_set:
            counter
            counter[i] = nums.count(i)
        
        while k > 0 :
            max_key = max(counter,key = counter.get)
            del counter[max_key]
            result.append(max_key)

            k -= 1
        return result