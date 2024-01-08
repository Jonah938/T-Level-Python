# This is a binary search algorithm made during week 03

## FUNCTION/PROCEDURE AREA ##
def binarySearch(items, toFind):
    # Find the first and last index within the list:
    iFirstIndex = 0

# This will give you the final item within the index:
    iLastIndex = len(items) - 1

    while(iFirstIndex<=iLastIndex):
        iMidIndex = (iFirstIndex + iLastIndex) // 2
        # Will be used to check if the middle of my list is the same as the number that I want to look for
        if items[iMidIndex] == toFind:
            print("YEs - the item exists")
            return 0 
        elif items[iMidIndex] < toFind:
            iFirstIndex = iMidIndex + 1
        else:
            iLastIndex = iMidIndex - 1

    print("Number is not in the list :(")
## MAIN AREA ##

# Create an ordered list of numbers (within a list)
iList = [1,15,16,18,20,27,30,105,177]
print("Here is a list of numbers:", iList)

# Ask the user to enter in a number that they would like to find
iSearchValue = int(input("Enter in a number that you want to search for: "))

# Run function
binarySearch(iList, iSearchValue)