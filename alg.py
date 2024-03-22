# strings are Unicode in python 3.x and later versions

# Greater Than Y. Create a function that accepts an array and returns the 
# number of values in that array whose value is greater than a given value y. 
# For example, if array = [1, 3, 5, 7] and y = 3, after your function runs your 
# function should return the number 2 (since there are two values in the array that are greater than 3)

def greaterThanY(arr,y):
    # initialize counter
    count = 0
    #iterate through array
    for value in arr:
        if value > y:
            count+= 1
    return count

array = [1, 3, 5, 7]
y = 3
result = greaterThanY(array, y)
print(result)

#  or 

def greater_than_y(arr, y):
    count = 0
    for i in range(len(arr)):
        if arr[i] > y:
            count += 1
    return count


print(greater_than_y([1, 2, 3, 4, 5, 6], 2))

# skip step up 3
string = "test this is step out"
print(string[3:18:3])

# Create a function that accepts a string of 1's and 0's and returns a count of all of the 1's in that string.
# Example: Given 1001011 returns 4 Hint: strings are just an array of chars that can't be altered. No built-in
# functions unless absolutely necessary

def strOfOnes(str):
    count = 0
    for i in str:
        if i == '1':
            count +=1
    print(count)

strOfOnes('1001011')

'''Create a function that accepts a string and returns that string but reversed. Eg. string returns gnirts
[::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, 
which means one step backwards.'''

def reverseStr(str):
    for value in str:
        return str[::-1]
str = reverseStr('string')
print(str)

# Given a string create a function that checks to see if a string is a palindrome. A palindrome is a 
# word that's spelled the same forward and backwards like racecar, mom dad Hint: reference reverse string
# algorithm. No built in functions unless absolutely needed.

def isPalindrome(x):
    if(x == x[::-1]):
        return 'yes'
    else:
        return 'no'
# x = 'mom' or:
x = input('enter string:')
print(isPalindrome(x))

# oop

class MyClass:
	x = 10
newObject=MyClass()
print(newObject.x) 

# Count Non-Spaces. Create a function that accepts a string and returns the number of non-space
# characters found in the string. Eg. "lol cool dude" return 11 not 13 NO builtin functions

def nonSpace(str):
    count = 0
    for char in str:
        if char != ' ':
            count += 1
    return count

str = "lol cool dude"
result=nonSpace(str)
print(result)

# Create function accepts input string and removes all white speces from that string. Given 
# "             whitespaces are cool           " return "whitespacesare cool" 

def remove_spaces(input_string):
    result = ''
    for char in input_string:
        if char != ' ':
            result += char
    return result

input_str = "             whitespaces are cool           "
result = remove_spaces(input_str)
print(result)

# Given an array w/only 2 values. Swap places of those 2 values and return the altered array.
# Given [1, 2] return [2, 1]

def swap_pairs(arr):
    # Swap the elements
    arr[0], arr[1] = arr[1], arr[0]
    return arr

print(swap_pairs([1, 2]))  # Output: [2, 1]
              
# Array swap pairs. Swap position of successive pairs of values of given array. If length is odd, do not
# change the final element. For [1, 2, 3, 4] return [2,1,4,3]. For eg. change input ["Brendan, true, 42"]
# to [true, "Brendan",42]. No build in array methods.

def swap_things(arr):
    # Function to swap pairs of values
    def swap(a, b):
        return b, a
    # initializes loop that iterates through arr in pairs the odd element is not addressed; start index 0 
    # to end-2nd to last thus len(arr) - 1 with a step of 2 (taking 2 at a time)
    for i in range(0, len(arr) - 1, 2):
        # arr[i] and arr[i+1] represents current pair of adjacent elements in array
        # swap function swaps these two elements
        arr[i], arr[i + 1] = swap(arr[i], arr[i + 1])

    return arr

print(swap_things([1, 2, 3, 4]))  # Output: [2, 1, 4, 3]
print(swap_things(["Brendan", True, 42]))  # Output: [True, 'Brendan', 42]
    
# Shift array values left shiftArrayValsLeft(arr). Given an rray, move all values forward (to the left
# by one index, dropping the first value and leaving a 0(zero) value at the end of the array.)
# Given [1,2,3,4,5] return [2,3,4,5,0].

lst = [1, 2, 3, 4, 5]

def shiftArrayValsLeft(arr):

  for i in range(len(arr)-1):
    arr[i] = arr[i+1]
  arr[len(arr)-1] = 0
  return arr

print(shiftArrayValsLeft(lst))

# Array: Push front given array and an additional value, create a function that inserts this value at the
# beginning of the array. Do this without using any built-in arra methods except push(). Given [2,3,4,5],1 return
# [1,2,3,4,5]

# 1. append val that's passed in as a param into the array [2,3,4,5,1]
# 2. Shift val from end to front so create for loop that starts at end of array and ends at beginning of array
# and for loop will decrement by 1
# 3. Swap 5 and 1, 4 and 1, 3 and 1 ... until 1 is at beginning of array shld look like [1,2,3,4,5]
# 4. Return array
# Does Thonny work on python?

def arrPushFront(arr, val):
    # #1
    arr.append(val)
    # #2
    for i in range(len(arr) - 1, 0, -1):
        #  #3
        temp = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = temp
        # first iteration would be [2,3,4,1,5]
    return arr
print(arrPushFront([2,3,4,5], 1))

# Array: Pop Front Given array, remove and return the value at the beginning of the array. 
# Do this without using any built-in array methods except pop(). Given [1,2,3,4,5] return 1 
# 1. Create for loop iterate from front of array to end of array
# 2. Inside loop swap value at current index w/value next to it
# [1,2] after swap [2,1];swap every value until first value is at end of array then pop
# 3. Once exit loop, pop off and return the last value in array

def arrPopFront(arr):
    # 1
    for i in range(0, len(arr)-1):
        temp = arr[i] # temp = 1 in first iteration
        arr[i] = arr[i+1] #[2,2,3,4,5]
        arr[i+1] = temp  #then [2,1,3,4,5]
    return arr.pop()
print(arrPopFront([1,2,3,4,5]))

# array min to front. Given a array of comparable values, move lowest element to array front,
# shifting backward any elements previously ahead of it. Don't otherwise change the array order.
# Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. 
#  1. for loop to iterate 
# 2. find minimum by comparing each number of two
# 3. swap min to front

def minFront(arr):
    min_index = 0 # initialize to keep track of variable for minimu element
    # Find the index of the minimum element in the array
    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    # arr.pop(min_index) removes element at index min_index from array and returns it
    # arr.insert(0,...) inserts the element returned by arr.pop(min_index) at beginning of array
            # take element at min_index remove it from current position and put it at beginning of array
    arr.insert(0, arr.pop(min_index))
    return arr

print(minFront([4, 2, 1, 3, 5]))  # Output: [1, 4, 2, 3, 5]



