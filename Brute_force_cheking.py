# List that contains integers
nums = [11,4,2,7,11,15]

# the target we want to get of the sum of two integers in num
target = 15

#Checks if a Number in the nums list is greater than the target -> if true its removing them from the list
def Check_for_greater(nums, target):
    while True:
        for x in nums: 
            #takes the highest int from the list and check if its bigger than the Target
            if max(nums) > target: 
                nums.remove(max(nums))
            #if there are no numbers bigger than the target, return the list
            else:
                return nums

#Checks if there are pairs in the list that sum up to the in of the target
def Conten_equals_Target(nums, target):
    #declaration of local varaibles
    index = 0
    firstInt = nums[index]
    iterations = 0
    #Dictionary which is important to track the amount of pairs since dicts are unique
    pairs = {}
    for x in range(len(nums)):
        #declaring the first int
        firstInt = nums[x]
        for y in range(x + 1, len(nums)):
            #declaring the second int
            secondInt = nums[y]
            #checking if the int sum up to the target
            if firstInt + secondInt == target:
                iterations += 1
                #saving the pair to ake them "unique"
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
