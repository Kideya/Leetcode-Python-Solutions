s = "III"
def RomanToInteger(s):
    conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    splitRoman = list(s)
    currentValue = 0
    skipNumber = False
    
    for i in range(len(splitRoman)):
            if i + 1 < len(splitRoman) and conversions[splitRoman[i]] < conversions[splitRoman[i + 1]] and not skipNumber:
                currentValue += (conversions[splitRoman[i + 1]] - conversions[splitRoman[i]])
                skipNumber = True
            elif skipNumber:
                skipNumber = False
            else:
                currentValue += conversions[splitRoman[i]]
    print(currentValue)    
    return currentValue
            
RomanToInteger(s)