
#List that contains integers
#nums = [2,7,11,15]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#the target we want to get of the sum of two integers in num
target = 9 

previousNumSize = None


def Check_for_greater(nums,target):
    while True:
        for x in nums:
            currentNumSize = len(nums)
            if max(nums) > target:
                nums.remove(max(nums))
            else:
                return nums
            
def Conten_equals_Target(nums,target):
    index = 0
    firstInt = nums[index]
    checkedPairs = 0
    amountOfPairs = 0
    
    for x in nums:
        if firstInt + x == target:
            print(f"Numbers which sum equals {target} are {firstInt} and {x}, total number of pairs in the List are {amountOfPairs} \n" 
                  f"amount of checked pairs are {checkedPairs}")
            amountOfPairs += 1
            index += 1
            firstInt 
        
        else:
            checkedPairs += 1
        
           
       
            

    
Check_for_greater(nums,target)
Conten_equals_Target(nums,target)