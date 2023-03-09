from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for elFirst in range(0,len(nums)):
        for elSecond in range(elFirst+1 , len(nums)):
            if(nums[elFirst] + nums[elSecond] == target):
                return [elFirst,elSecond]
    return

a = [2,7,11,15]
b = 9
print(twoSum(a,b))