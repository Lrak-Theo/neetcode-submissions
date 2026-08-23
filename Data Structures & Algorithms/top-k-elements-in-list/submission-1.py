class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_map = {}
        count_array = [ [] for i in range(len(nums)+1)]

        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1
        
        for num, count in nums_map.items():
            count_array[count].append(num)
        
        result = []
        for x in range(len(count_array)-1, 0, -1):

            for n in count_array[x]:
                result.append(n)

                if len(result) == k:
                    return result