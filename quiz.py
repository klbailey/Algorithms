# Print 1-255 print1To255(). Print all the integers from 1 to 255.

def allInt():
    for i in range(1, 256):
        print (i)
allInt()

# Print Ints and Sum 0-255 printIntsAndSum0To255(). Print integers from 0 to 255, and with each integer print the sum so far. 

def printIntsAndSum0To255():
    sum = 0
    for i in range(1, 256):
        print(i)
        sum += i
        print(sum)       
printIntsAndSum0To255()

# Print Odds 1-255 printOdds1To255(). Print all odd integers from 1 to 255

def printOdds1To255():
    for i in range(1, 256):
        if i % 2 == 0:
            print(i) 
printOdds1To255()

# Print Array Values printArrayVals(arr). Iterate through a given array, printing each value.
arr = ['Hi', 'Hello', 1]
def printArrayVals(arr):
    for i in arr:
        print(i)
printArrayVals(arr)

# Return Odds Array 1-255 returnOddsArray1To255(). Create and return an array with all the odd integers between 1 and 255 (inclusive).

def returnOddsArray1To255():
    arr = []
    for i in range(1, 256):
        if i % 2 != 0:
            print(i)
returnOddsArray1To255()

# Print Max of Array printMaxOfArray(arr). Given an array, find and print its largest element.

def printMaxOfArray(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
print(printMaxOfArray([1, 3, 5, 7, 9, 0, 2, 4, 6]))

# Print Average of Array printAverageOfArray(arr). Analyze an array’s values and print the average.

def printAverageOfArray(arr):
    sum = 0
    for i in arr:
        sum += i
    avg = sum / len(arr)
    return avg
print(printAverageOfArray([1, 3]))

# Print Max, Min, Average Array Values printMaxMinAverageArrayVals(arr). 
# Given an array, print the max, min and average values for that array.

def printMaxMinAverageArrayVals(arr):
    max = arr[0]
    min = arr[0]
    sum = 0
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    for i in arr:
        sum += i
        avg = sum / len(arr)   
    return max, min, avg

print(printMaxMinAverageArrayVals([1,3,2]))

# Return Array Count Greater than Y returnArrayCountGreaterThanY(arr, y). Given an array and a value Y, 
# count and print the number of array values greater than Y. Given [1,2,3,4,5], Y = 3 return 2 (because 
# there are 2 values in the array that are greater than 3.

def returnArrayCountGreaterThanY(arr, y):
    count = 0
    for value in arr:
        if value > y:
            count+= 1
    return count

print(returnArrayCountGreaterThanY([1,2,3,4,5], 3))

# Swap String for Array Negative Values swapStringForArrayNegativeVals(arr). Given an array of numbers, 
# replace any negative values with the string 'Skillspire'.

# Square Array Values squareArrayVals(arr). Square each value in a given array, returning that same array with 
# changed values. Given [1,2,3,4,5] return [1,4,9,16,25]

# Shift Array Values Left shiftArrayValsLeft(arr). Given an array, move all values forward (to the left) by one 
# index, dropping the first value and leaving a 0 (zero) value at the end of the array. Given [1,2,3,4,5] return [2,3,4,5,0]

#  Given an array with only 2 values. Swap the places of those 2 values and return the altered array. Given [1,2] return [2,1]

# Array swap pairs. Swap positions of successive pairs of values of a given array. If length is odd, do not change the 
# final element. For [1,2,3,4], return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42]. 
# As with all array challenges, do this without using any built-in array methods.