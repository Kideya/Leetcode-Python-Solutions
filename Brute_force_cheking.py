# List that contains integers
nums = [11,4,2,7,11,15]

# the target we want to get of the sum of two integers in num
target = 15

def Check_for_greater(nums, target):
    while True:
        for x in nums:
            if max(nums) > target:
                nums.remove(max(nums))
            else:
                return nums

def Conten_equals_Target(nums, target):
    index = 0
    firstInt = nums[index]
    iterations = 0
    pairs = {}
    for x in range(len(nums)):
        firstInt = nums[x]
        for y in range(x + 1, len(nums)):
            secondInt = nums[y]
            if firstInt + secondInt == target:
                iterations += 1

                pairs.update({firstInt: secondInt})

                print(
                    f"The pair {firstInt} and {secondInt} are equal to {target}\n"
                    f"it took {iterations} iterations to find this pair and theire are a total of {len(pairs)} pairs \n"
                )

                print(f"{pairs}\n")
            else:
                iterations += 1

Check_for_greater(nums, target)
Conten_equals_Target(nums, target)
