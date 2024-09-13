# Book index. Given an array of numbers (book page numbers) return a string
# containing the same numbers in sequential order. If the numbers are in
# consecutive add a dash between the first number in the sequence and the
# last number in the sequence. Given [1,13,14,15,16,37,38,39,70] =>
# "1,13-16,37-39,70"

# 1. Create a function that takes an array as a parameter
# 2. Create an empty string variable for out output string
# 3. Create a for loop that iterates through the list of numbers
# 4. Is first number part of a sequence-keep track of current index in a variable.
#    Add value at current index to output string
# 5. While the next number is consecutive, incrment index and continue tracking/while loop and counter
# 6. If current index is > current index variable  add a dash and the last number in range
# 7. Return the range of strings

'''First Run:

    While loop condition: 0 + 1 < len(arr) and arr[1] == arr[0] + 1
        Since arr is [1, 13, 14]:
            0 + 1 < len(arr) becomes 1 < 3
            arr[1] == arr[0] + 1 becomes 13 == 1 + 1, which is False.
    Since the condition is False, the loop terminates without incrementing i.
    i remains 0.
    currentIndex remains 0.
    No range is formed (i didn't change), so "1" is appended to pages.
    Since i + 1 is still less than len(arr), a comma is appended to pages.
    i is incremented by 1.
    pages after the first run: "1"'''

def book_index(arr):
    pages = "" # 1 and , go in after 1st run then 13

    i = 0
    while i  < len(arr):
        pages += str(arr[i]) #1 goes to pages
        currentIndex = i # stores 0 the current index 
        # first run 
        while i + 1 < len(arr) and arr[i+1] == arr[i] + 1:
        # While loop condition: 0 + 1 < len(arr) and arr[1] == arr[0] + 1
            i+=1 #increment by 1 because 13 is [1] and 13 == 1+1
            # arr[1] == arr[0] + 1 becomes 13 == 1 + 1, which is False.
            '''Since the condition is False, the loop terminates without incrementing i.
    i remains 0. currentIndex remains 0. No range is formed (i didn't change), so "1" is appended to pages'''

        if i > currentIndex:
            pages += f"-{arr[i]}" # puts in -16

        # Since i + 1 is still less than len(arr), a comma is appended to pages.
        # i is incremented by 1.
        if i + 1 < len(arr):
            pages += ","

        i+=1

    return pages


print(book_index([1,13,14,15,16,37,38,39,70]))

#

'''
Write a function that accepts as a parameter a string containing someone’s name. Return a 
string containing the following oh-so-cool greeting: strip off the first letter of the name, 
capitalize this new word, and add " to the [first letter]!" Given "Dylan", return "Ylan to the D!"​
'''
def cool_greeting(name):
    new_name = name[1:].capitalize()
    return f"{new_name} to the {name[0]}!"

name = "Dylan"
print(cool_greeting(name))  # Output: Ylan to the D!

'''
Acronyms. Create a function that, given a string, returns the string’s acronym (first letters only, 
capitalized). Given "there's no free lunch gotta pay yer way", return "TNFLGPYW". Given "Live from 
New York it's Saturday Night", return "LFNYISN".
'''
def acronym(string):
    words = string.split()
    acr = ""
    for word in words:
        acr += word[0].upper()
    return acr

string1 = "there's no free lunch gotta pay yer way"
string2 = "Live from New York it's Saturday Night"

print(acronym(string1))  # Output: TNFLGPYW
print(acronym(string2))  # Output: LFNYISN

'''Write a function that accepts as a parameter a string containing someone’s name. Return a string containing
the following oh-so-cool greeting: strip off the first letter of the name, capitalize this new word, and add
" to the [first letter]!" Given "Dylan", return "Ylan to the D!"​'''

#1. Create a function with the correct parameters
#2. Create a variable for the output string. Assign the string to string[1].upper()
#3. Create a for loop that interates through the string and copies the rest of the characters
#in the name
#4. Hard code the rest of the string by adding "to the string[0]!"
#5 Return output string

def coolGreeting(string):
    output = string[1].upper()

    for i in range(2, len(string)):
        output += string[i]

    return output + f" to the {string[0]}!"

print(coolGreeting("Tom"))

'''Acronyms. Create a function that, given a string, returns the string’s acronym (first letters only, capitalized).
Given "there's no free lunch gotta pay yer way", return "TNFLGPYW". Given "Live from New York it's Saturday Night",
return "LFNYISN".'''

#1. Create the function and pass the correct arguments
#2. Create an output string add and capitalize the first character of the input
#string  output = string[0].upper()
#3. Iterate through the string using a for loop. Start at index 1
#4. inside of the for loop, check to see if the character before the current character is a space
#if it is a space then that indicates that the current character is the start of a new word
#5. Captialize current character and add to the output string.
#6. return output string

def acronym(string):
    output = string[0].upper()

    for i in range(1,len(string)):
        if string[i-1] == " ":
            output += string[i].upper()


    return output

print(acronym("there's no free lunch gotta pay yer way"))

'''
Array: Remove Duplicates. Remove array duplicates. Do not alter original. 
Return new array with results ‘stable’ (original order). For [1,2,1,3,4,2,1] return [1,2,3,4].​
'''
def remove_duplicates(arr):
    # Blank dictionary
    seen = {}
    # blank list
    result = []
    for item in arr:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result

arr = [1, 2, 1, 3, 4, 2, 1]
result = remove_duplicates(arr)
print(result) 

'''
or
1. Create a function with the correct params
2. Create a variable that stores an empty array
3. Create a for loop to iterate through array
4. Inside for loop check if value exists in output array
5. If value doesn't exist appned that value into the output array
6. Return output array
Didn't work for me:
'''
# def removeDupes(arr):
#     output = []

#     for val in arr:
#         if val in arr: 
#             output.append(val)
#     return output

# arr = [1, 2, 1, 3, 4, 2, 1]
# output = removeDupes(arr)
# print(output) 


'''
Parens Valid. Create a function that, given an input string str, 
returns a boolean whether the parentheses in str are valid. Valid sets of parentheses 
always open before they close, for example. For "(()())", return true. Given "(()", 
return false: not every parenthesis is closed. Given "())(", return false, because the 
underlined ")" is premature: there is nothing open for it to close.
'''

def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False

    return stack == []

print(is_valid_parentheses("(()())"))  # Output: True
print(is_valid_parentheses("(()"))      # Output: False
print(is_valid_parentheses("())("))      # Output: False


'''
or
1. Create function and pass in corret params
2. Create variable and assign it to an empty list
3. Iterate through our strong of parenthesis
4. If the value at current index is an opening parenthesis push to output lsit
5. If value is closing parentheses pop off the last val in  list
6. Return if output list is empty or not
'''
def parensValid(string):
    output = []

    for val in string: 
        if(val == "("):
            output.append("(")
        else:
            output.pop()


    return len(output) == 0

print(parensValid("(()())"))
print(parensValid("(()"))

'''Big O Notation-describes how fast a computer runs. O(1) Constant Time Complexity (no loops):
def accessElement(arr):
    arr.pop()
    returnarr[0]
    
O(N) Linear Time Complexity-execution time increases linearly with size of input data:
(one loop usually)
def arrPushFront(arr,val):
    arr.append(val)
    for i in range(len(arr) -1, 01, -1):
        temp = arr[i]
        arr[i] = arr[i-1]
        arr[i=1] = temp
    return array
    
O(Nsquared) - example: nested loop for each element
def acccess(arr):
    for i in range(len(arr))
        print(i)
        for j in range(len(arr)):
            print(j)
    return arr
    
Array: Flatten a given array, eliminating nested & empty arrays. 
Don't alter; return a new one retaining order For [1,[2,3],4[]] 
return [1,2,3,4]'''

def flatten_array(arr):
    flattened = []
    for item in arr:
        # True if specified object is of specified type 
        # Is current item a list
        if isinstance(item, list):
            # if current item is a list recursively calls flatten_array
            # extend adds all elements of flattened list to flattened []
            flattened.extend(flatten_array(item))
            # if not a list if it's not 'None'
        elif item is not None:
            #append to flattened []
            flattened.append(item)
    return flattened

input_array = [1, [2, 3], 4, []]
output_array = flatten_array(input_array)
print(output_array) 

#instructor solution:

# def arrFlat(arr):
#     output = []
#     for val in arr:
#         if type(val) == list:
#             for num in val:
#                 output.append(num)
#         else:
#             output.append(val)

# print(arrFlat([1, [2, 3], 4, []]))
    
'''Array: mode. Create a function that given an array returns most frequent
value in array Given [1,2,2,3,4,5] return 2. Hint: use dictionary
    '''

def find_mode(arr):
    # Dictionary store the frequency each element
    freq_dict = {}
    
    # Iterate &  count the occurrences each element
    for num in arr:
        # is num in dictionary
        if num in freq_dict:
            # counts one more occurrence of the num element
            freq_dict[num] += 1
            # if num not already a key in {}
        else:
            # element num  as the key and assigns its value to 1 encountered once
            freq_dict[num] = 1
    
    
    # calculates the maximum frequency (count) of any element in the freq_dict dictionary
    # freq_dict.values() retrieves all the values(frequencies) from dictionary; ea
    # value represents count of occurrences of a specific element in input array 
    max_freq = max(freq_dict.values())
    ''' freq_dict.items(): retrieves key-value pairs from  freq_dict dictionary, where each key is an element from
    input array & each value is its corresponding frequency. for key, value in freq_dict.items(): 
    This iterates over each key-value pair in freq_dict. if value == max_freq: This conditional 
    statement checks if current frequency (value) is equal to  maximum frequency (max_freq). key: 
    This is  key (element) from the dictionary, representing an element from input array. [key for key,
    value in freq_dict.items() if value == max_freq]: This is a list comprehension that creates a list 
    of keys for which the corresponding value (frequency) is equal to max_freq. In other words, it 
    collects all the elements that have the maximum frequency. max_freq will contain maximum frequency 
    found in the input array. mode will contain a list of all elements (keys) from input array that 
    have the maximum frequency. These are the mode(s) of the array, i.e., 
    the element(s) that appear most frequently.
    '''
    mode = [key for key, value in freq_dict.items() if value == max_freq]
    
    return mode


arr = [1, 2, 2, 3, 4, 5]
result = find_mode(arr)
print("Mode:", result)

# Instructor solution: key is '2' val is 1 and when second 2 key is 2 val is 2

def modem(arr):
    tracker = {}
    for val in arr:
        if val in tracker:
            tracker[val] = tracker[val] + 1
        else:
            tracker[val] = 1
    maxOccurance = -1
    maxKey = arr[0]
    for key in tracker:
        if tracker[key] > maxOccurance:
            maxKey = key
            maxOccurance = tracker[key]
    return maxKey

print(modem([1, 2, 2, 3, 4, 5]))

'''
Given 2 arrays that are sorted but not necessarily the same length, find the median value.
Given ([1,5,9],[1,2,3,4,5,6]) return 4. If the number of values is even, return the average
of the two middle values. Given ([1,5,9],[1,2,3,4,5]) return 3.5
'''
def findMedianSortedArrays(nums1, nums2):
    # Calculate the total length of the merged array
    total_length = len(nums1) + len(nums2) # 8
    
    # Initialize an empty list to store the merged array
    merged = []
    
    # Initialize pointers for both arrays
    i = j = 0

    # Merge the arrays while both pointers are within their respective arrays
    while i < len(nums1) and j < len(nums2):
        # Compare elements at current positions in both arrays
        # Append the smaller element to the merged array
        if nums1[i] <= nums2[j]: # 3 < 5
            merged.append(nums1[i]) #1, 5, 9 go into merged[]
            i += 1 # go through 1, 5, 9
        else: # if nums2 <= nums1
            merged.append(nums2[j]) #1,2,3,4,5 go into merged[]
            j += 1 # go through 1,2,3,4,5

    # If any elements are remaining in the first array, append them to the merged array
    merged.extend(nums1[i:]) # none in this example
    
    # If any elements are remaining in the second array, append them to the merged array
    merged.extend(nums2[j:]) # put 1,2,3,4,5 in merged[] after 1,5,9 so its 1,5,9,1,2,3,4,5

    # Check if the total number of elements in the merged array is even
    if total_length % 2 == 0: # it is because 8 
        # If even, calculate the median as the average of the two middle elements
        mid = total_length // 2 # 8 / 2 = 4
        return (merged[mid - 1] + merged[mid]) / 2 # 4-1=3 + 4 = 7 / 2 = 3.5
    else:
        # If odd, return the middle element as the median
        return merged[total_length // 2] 

result2 = findMedianSortedArrays([1,5,9], [1,2,3,4,5])
print(result2)  

'''Instructor solution:'''

def findMedian(arr1,arr2):
    combinedArr = sorted( arr1 + arr2 ) #Combine and sort arrays

    middleIndex = round(len(combinedArr)/2)

    if len(combinedArr) %  2 == 0:
        return (combinedArr[middleIndex] + combinedArr[middleIndex - 1]) / 2

    return combinedArr[middleIndex]

'''
Create a function that, given a string of words (with spaces), returns a new string with words
in reverse sequence. Given "This is a test", return "test a is This".Hint: Look up string.split()​

You may use helper functions like .concat(), split(), and join() 
'''

def reverse_words(sentence):
    # Split the sentence into a list of words in array
    words = sentence.split() #'This' 'is' 'a' 'test'
    
    # Reverse the order of the words; :: slice entire list -1 iterate(step) over list in reverse order 
    reversed_words = words[::-1] # 'test', 'a', 'is', 'This'
    
    # Join the words back into a single string with spaces (space separator)
    # ['test', 'a', 'is', 'This'] becomes 'test a is This'
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

original_sentence = "This is a test"
reversed_sentence = reverse_words(original_sentence)
print(reversed_sentence)  

'''Instructor solution:'''

def reverseSentence(string):
    wordArr = string.split() #Split string ["This","is","a","test"]
    wordArr = tuple(reversed(wordArr)) #("test", "a", "is","This")

    return " ".join(wordArr)

print(reverseSentence("This is a test"))


