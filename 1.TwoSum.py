# List that contains integers
nums = [12, 43, 5, 17, 28, 33, 7, 50, 29, 18, 
22, 9, 44, 3, 20, 16, 40, 27, 31, 6, 
14, 49, 21, 35, 2, 19, 25, 47, 38, 34, 
11, 30, 4, 46, 15, 8, 36, 41, 48, 23, 
24, 39, 10, 45, 37, 26, 32, 13, 1, 42, 
4, 16, 35, 11, 18, 48, 7, 19, 25, 29, 
21, 3, 50, 47, 44, 39, 27, 5, 22, 12, 
14, 41, 38, 46, 31, 28, 17, 20, 34, 9, 
15, 24, 49, 1, 36, 13, 42, 43, 26, 6

]

# the target we want to get of the sum of two integers in num
target = 20

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
                #saving the pair to ake them "unique" also checking if one is bigger than the other to have no doubles
                if firstInt >= secondInt:
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
