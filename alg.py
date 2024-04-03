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

def swap_pairs(arr):
    # If the length of the array is odd, leave the last element unchanged
    if len(arr) % 2 != 0:
        last_element = arr.pop()
    else:
        last_element = None
        
    # Iterate through the array in steps of 2
    for i in range(0, len(arr) - 1, 2):
        # Swap pairs of elements
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Append the last element back if it exists
    if last_element is not None:
        arr.append(last_element)

    return arr

# Test cases
print(swap_pairs([1, 2, 3, 4]))  # Output: [2, 1, 4, 3]
print(swap_pairs(["Brendan", True, 42]))  # Output: [True, 'Brendan', 42]

    
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
    arr.append(val) #becomes [2,3,4,5,1]
    # #2
    for i in range(len(arr) - 1, 0, -1): #backward from right to left
        #  #3
        temp = arr[i] # i starts at index 4 which is value 1 so temp becomes 1
        arr[i] = arr[i-1] # starts with value at index i-1 which is 5; put 5 in index i;becomes [2,3,4,5,5]
        arr[i-1] = temp #put 1 as arr[i-1] and it becomes [2,3,4,1,5]
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

# Given 2 arrays zip them together: given [1, 3, 5] [2,4] return [1,3,5,2,4] Doesn't have to be ordered.
# No built in methods except push and pop

def arrZip(arr1, arr2):
    # initialize to storearr1 and arr2 combined elements
    result = []
    # iterate thru arrays
    while arr1:
        # take the first item from arr1 and put it at the end of the result list.
        # len(result) current length of result list
        # 
        result[len(result):len(result)] = [arr1.pop(0)]
    while arr2:
        # take the first item from arr1 and put it at the end of the result list.
        # takes 1 from arr1 and puts it in result
        result[len(result):len(result)] = [arr2.pop(0)]

    return result

arr1 = [1,3,5]
arr2 = [2,4]
result=arrZip(arr1, arr2)
print(result)

# Remove shorter strings. Given string array and value (length), remove any strings shorter than length from the
# array. Given (["you","i","ab"], 3) return ["you"]. You can use any functions that you have created. Hint
# removeAt() or find a method that removes a vlaue from an array

def abc(arr, x):
    # string for string in arr iterates over each string in arr list
    return [string for string in arr if len(string) >= x]

arr=["you","i","ab"]
x=3
print(abc(arr,x))

# Remove even-length strings. Build a standalone function to remove strings of even lengths from a given array.
# For array containing ["Nope!","its","Kris","starting","with","K!","(instead","of","Chris","with","C)","."],"
#  change array to ["Nope!","its", "Chris","."]

def abc(arr):
    return [string for string in arr if len(string) % 2 != 0]

arr = ["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."]
arr = abc(arr)
print(arr) 

# Given a string of words (sentence) create a function that capitalizes every word in the string. Given
# 'hello there skillspire' return 'Hello There Skillspire'. No built in methods except the one that
# capitalizes a character. (hint if there's a space in between 'there' and 'skillspire' is key indicator)

def capitalize(str):
    # empty but will hold string
    capSentence = ""
    # flag to indicate whether the next character should be capitalized
    capNext = True
    # iterate
    for char in str:
    # if current char is a space
        if char == ' ':
             # Set the flag to capitalize the next character
            capNext = True
            # add the space character to capSentence 
            capSentence += char
         # If the flag is set to capitalize the next character
        elif capNext:
            # Capitalize the current character and add it to the capitalized sentence
            capSentence += char.upper()
            # Reset flag to indicate that the next character should not be capitalized
            capNext = False
        else:
            # Add current character to the capitalized sentence without capitalization
            capSentence += char
        
         # Return the final capitalized sentence
    return capSentence

str = "hello there skillspire"
result = capitalize(str)
print(result)

# Second option:
def capitalizeSentence(string):
    output = string[0].upper() #'h' will be 'H'
    for i in range(1, len(string)):
        output += string[i].upper()
    else:
        output += string[i] # no space before concatenate
    return output

str = "hello there skillspire"
result = capitalize(str)
print(result)


# Create a standalone function that accepts an input string, removes leading and trailing white spaces 
# (at beginning and end only) from teh string and capitalize the first letter of every word and return
# that string '           whitespaces    are  cool     '
# return 'Whitespaces Are Cool' don't use trim. Find character that's not space in beginning of string?

def process_string(input_string):
    # Remove leading and trailing spaces
    input_string = remove_spaces(input_string)
    # Initialize an empty string to store the final result
    result_string = ""
    # Flag to indicate whether the next character should be capitalized
    capitalize_next = True  
    # Loop through each character in the input string
    for char in input_string:
        if char == ' ':  # If the current character is a space
            capitalize_next = True  # Set the flag to capitalize the next character
            if result_string and result_string[-1] != ' ':  # Check if the previous character is not a space
                result_string += char  # Add the space character to the result string
        elif capitalize_next:  # If the flag is set to capitalize the next character
            result_string += capitalize_char(char)  # Capitalize the current character
            capitalize_next = False  # Reset the flag
        else:
            result_string += char.lower()  # Add the current character as lowercase
            
    return result_string

# Function to remove leading and trailing spaces
def remove_spaces(input_string):
    # Initialize variables to track start and end indices of non-space characters
    start_index = 0
    end_index = len(input_string) - 1
     # Find the index of the first non-space character from the beginning of the string
    while start_index <= end_index and input_string[start_index] == ' ':
        start_index += 1
    # Find the index of the last non-space character from the end of the string
    while end_index >= start_index and input_string[end_index] == ' ':
        end_index -= 1
    # Return the substring of the input string excluding leading and trailing spaces
    return input_string[start_index:end_index+1]

# Function to capitalize a character
def capitalize_char(char):
    # Check if the character is a lowercase letter
    if 'a' <= char <= 'z':
        # Convert the lowercase letter to uppercase using ASCII values
        # Subtract the ASCII value of 'a' from the ASCII value of the character
        # Add the result to the ASCII value of 'A' to get the corresponding uppercase letter
        return chr(ord(char) - ord('a') + ord('A'))
    # If the character is not a lowercase letter, return it unchanged
    return char

# Example usage:
input_string = '           whitespaces    are  cool     '
result = process_string(input_string)
print(result)  # Output: 'Whitespaces Are Cool'

# or which doesn't work?:
def removeWhitespaces(string):
    start = 0
    end = len(string) - 1

    while string[start] == " ":
        start += 1

    while string[end] == " ":
        end -= 1

    return capitalizeSentence(string[start:end])

print(removeWhitespaces("       this is a sentence     "))