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