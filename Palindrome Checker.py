import math
target = 120032940
isPalindrome = None
slicedTarget = []


def CreateListLength(target):
    potence = 1
    x = 0
    
    while x  <= target:
        x = pow(10,potence)
        potence += 1
        
    if x >= target:
        potence -= 1
        listLength = potence 
        print(f"The Number has {potence} digits")
        
    while listLength > 0:
        slicedTarget.append("")
        listLength -= 1
    
    if listLength == 0:
        return (potence -1)

def sliceNumber(slicedTarget,target,potence):
    index = 0
    while target > 10:
        FirstTarget = target / pow(10,potence)
        FirstTarget = math.floor(FirstTarget)
        target -= FirstTarget * pow(10,potence)
        potence -= 1
        slicedTarget[index] = FirstTarget
        index += 1
        print(FirstTarget,slicedTarget) 
    
    for x in range(len(slicedTarget)):
        if isinstance(slicedTarget[x],str):
            slicedTarget[x] = 0
            print(slicedTarget)
        
    
sliceNumber(slicedTarget,target,CreateListLength(target))