import math

initialTarget = 112211  # The initial Integer that need to be checked
target = initialTarget  # Variable for the calculations
isPalindrome = None  # Variable for showing if it is a palindrome or not
slicedTarget = []  # List for saving the digits of the target

def CreateListLength(target):
    """
    Calculates the number of digits in the given number and creates a list to store those digits.

    Parameters:
    target (int): The number for which the digit count is to be calculated.

    Return value:
    int: The number of digits in the number, reduced by 1.
    """
    
    potence = 1  # Start amount for the potence
    x = 0  # Variable for calculating the power of 10.
    
    # Calculation for the amount of digits of the target
    while x <= target:
        x = pow(10, potence)
        potence += 1
        
    if x >= target:
        potence -= 1
        listLength = potence 
        
    #Initializing the List for storing the digits
    while listLength > 0:
        slicedTarget.append("")
        listLength -= 1
    
    if listLength == 0:
        return (potence - 1)  # Returns amount of digits

def SliceNumber(slicedTarget, target, potence):
    """
    Splits the given number into its digits and checks if the number is a palindrome. A palindrome is a number that reads the same forwards and backwards.

    Parameters:
    slicedTarget (list): The list where the digits of the number will be stored.
    target (int): The number to be split into digits.
    potence (int): The number of digits in the number.

    Return value:
    None
    """
    index = 0  # Startindex for the digits
    amountOfdigits = potence  # Amount of digits

    # Slicing the target into digits
    while target != 0:
        FirstTarget = target / pow(10, potence)  # Calculation for the current digit
        FirstTarget = math.floor(FirstTarget)  # Round off to a single digit
        target -= FirstTarget * pow(10, potence)  # Removing the current Number from the target
        potence -= 1  # Reducing the potence
        slicedTarget[index] = FirstTarget  # Saving the digit to the List
        index += 1
        
    # Removing digits from the beginning and end of the list when they are equal.
    while slicedTarget[len(slicedTarget)-1] == slicedTarget[0] and amountOfdigits != 0:
        del slicedTarget[len(slicedTarget)-1]  # Löschen der letzten Ziffer
        del slicedTarget[0]  # Löschen der ersten Ziffer
        amountOfdigits -= 1
        
        # Break when only one digit is left.
        if len(slicedTarget) <= 1:
            print(f"Länge:{len(slicedTarget)}")
            break
        
    # Checking if the number is a palindrome.
    if len(slicedTarget) <= 1:
        print(f"The Number {initialTarget} is a palindrome")
        isPalindrome = True
        return isPalindrome
    else:
        print(f"The Number {initialTarget} is not a palindrome")
        isPalindrome = False
        return isPalindrome

# Calling the function to split the number into digits and check for palindrome.
SliceNumber(slicedTarget, target, CreateListLength(target))