target = 1
isPalindrome = None

def SliceTarget(target):
    potence = 1
    x = 0
    while x  <= target:
        x = pow(10,potence)
        potence += 1
        print(x)
    if x >= target and target < 999:
        potence -= 1
        print(f"The Number has {potence} digits")
    elif x>= target:
        potence += 1
        print(f"The Number has {potence} digits")

SliceTarget(target)