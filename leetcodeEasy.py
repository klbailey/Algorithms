'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of elements
        num_indices = {} #1st iteration empty
        
        # Traverse the array; enumerate function is a built-in function that allows you to iterate 
        # through a sequence and keep track of the index of each element. This function can be useful if you
        # need to access the index of each element in the sequence.
       
        for i, num in enumerate(nums): #1st iteration i=0 nums=2
            # Calculate the complement required to reach the target
            # compliment is a concept (find pair that equals target)
            complement = target - num # target=9 num=2 complement is 9-2=7
            
            # check if calculated complement exists in num_indices dictionary;
            #it's empty in 1st interation so skip the block
            if complement in num_indices:
                # If found, return the indices of the current element and its complement
                return [num_indices[complement], i]
            
            # Store the index of the current number in num_indices
            # num=2 i=0 so num_indices[2] = 0 during 1st iteration
            num_indices[num] = i 
        
        # If no solution is found, return an empty list
        return []
    
nums = [2,7,11,15]
target = 9 
solution = Solution()
print(solution.twoSum(nums, target)) #output [0,1]

'''Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1: Input: x = 121 Output: true
Explanation: 121 reads as 121 from left to right and from right to left.'''

# (x: int) parameter x should be integer
# -> bool indicates return type of the function should be bool (true or false)
def isPalindrome(x: int) -> bool:
    # Convert the integer x to a string using str(x) for easier comparison
    num_str = str(x)
    
    # Check if the string representation of the number is equal to its reverse
    # use slicing [::-1] to reverse string (creates reversed version)
    # if num_str != num_str[::=1] it will return false
    return num_str == num_str[::-1]

x = 121
result = isPalindrome(x)
print(result)  # Output: True

'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II. Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract 
it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is 
used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.'''

def romanToInt(s: str) -> int:
    # Create a dictionary to map Roman numerals to their integer values
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize the result
    result = 0
    
    # Iterate through the string
    for i in range(len(s)):
        # Get the integer value of the current Roman numeral; 
        # 1st iteration i=0 s[i]=I get integer value of I from roman_values: value=1; add value to result result+=1
        # 2nd iteration i=1 s[i]=I get integer value of I from roman_values: value=1; add value to result result +=1
        # 3rd iteration i=2 s[i]=I get integer value of I from roman_values: value=1; add value to result result+=1
        # return result which is 3
        value = roman_values[s[i]]
        
        # If the current Roman numeral represents a smaller value than the next Roman numeral, subtract its value
        # needed example IV 4 V - I; if we encounter a char whose value is less than value of the next char, it
        # indicates we need to subtract the current value from the next value
        # if i < len(s) - 1 ensures we don't try to access an index beyond the end of the string
        # roman_values[s[i]] < roman_values[s[i + 1]]: checks value of roman number at current index i is less than next roman number
        # then we subtract it 
        if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            result -= value
        else:
            result += value
    
    return result

# Example usage:
s = "III"
print(romanToInt(s))  # Output: 3

'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. '''

def longestCommonPrefix(strs):
    if not strs:  # Check if the input list is empty
        return ""  # If empty, return an empty string

    # Initialize the longest common prefix as the first string in the list
    prefix = strs[0] # eg. 'flower'

    # Iterate through the strings starting from the second string; eg strs[1:] is 'flow', 'flight'
    for string in strs[1:]:
        # Compare each character of the current string with the prefix until mismatch or end of string
        # eg. comparing 'flow' with 'flower' common prefix 'fl'; comparing 'flight' with 'fl' common previx 'fl'
        # final prefix 'fl' output 'fl'
        i = 0
        # while i < len(prefix) don't go beyond length of current prefix string while comparing characters; i < 'flower' i<6
        # i < len(string) don't go beyond length of current string while comparing characters; flow 4 
        # prefix[i] == string[i] check char at index-[0]='f'? [1]='l'? [2]='o'? [3]= w? [4]=e? no then stops
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1
        
        # Update the prefix to the common prefix up to the current index; flower, flow, flight: prefix is flower
        # i=2 ('fl') because that's where there's a mismatch in flight
        # prefix[:i] includes characters from index 0 up to index 2, but not including index 2 itself
        prefix = prefix[:i]
        
        # If the prefix becomes empty, break the loop
        if not prefix:
            break

    return prefix

# Example usage:
strs1 = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs2))  # Output: ""

'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 Example 1:
Input: s = "()"
Output: true
 Example 2:
Input: s = "()[]{}"
Output: true
 Example 3:
Input: s = "(]"
Output: false'''

def isValid(s: str) -> bool:
    # Create a dictionary to map closing brackets to their corresponding opening brackets using key value pairs
    # ')' is key paired with value '('
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Initialize an empty stack that will hold opening brackets encountered in string 's'
    # stack data structure is a data structure that follows the Last-In-First-Out (LIFO) principle. 
    # This means the last element added to the stack will be the first one to be removed.
    stack = []
    # Iterate through each character in the string
    for char in s:
        # If the character is an opening bracket, push it onto top of the stack
        if char in bracket_map.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_map.keys():
            # Check if the stack is empty or the topmost opening bracket doesn't match eg. (]
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # If it matches, pop the topmost opening bracket from the stack
            stack.pop()
        # If the character is neither an opening nor a closing bracket, skip it
        else:
            continue
    # After iterating through the entire string, check if the stack is empty
    return not stack

# Test cases
print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False

'''You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be 
made by splicing together the nodes of the first two lists.Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order. '''

# class represents a single node in a linked list w/2 attributes: 'val' stores value and 'next' points to next node in list
# ListNode keeps track of every number in the 2 lists. Each ListNode represents a single # in our list to maintain order
# and ensures they are connected properly when we merge the list
class ListNode:
    # def __init__(self, val=0, next=None): is the recipe or method for new node in our linked list
    def __init__(self, val=0, next=None):
        # tells new node what value it should hold eg. if node is for 5 val would be 5
        self.val = val
        # tell new node where to find next node in list; if next node is 7 'next' will point to that node
        self.next = next

# Define a function to merge two sorted linked lists
def mergeTwoLists(list1, list2):
    # Create a dummy node to serve as the starting point of the merged list 
    dummy = ListNode()  # Initialize an empty dummy node
    # Create a pointer to keep track of the current node in the merged list
    current = dummy
    
    # While both lists have nodes
    while list1 and list2:
        # Compare the values of the current nodes in list1 and list2
        '''1st Iteration:
           list1: [1] -> [2] -> [4] -> None
           list2: [1] -> [3] -> [4] -> None '''
        if list1.val <= list2.val:
            # If the value in list1 is smaller or equal, append it to the merged list
            '''merged list [1]'''
            current.next = list1  # Append the current node of list1 to the merged list
            # Move to the next node in list1
            '''update pointers
               list1: [2] -> [4] -> None
               list2: [1] -> [3] -> [4] -> None '''
            list1 = list1.next  # Move the list1 pointer to the next node
        else:
            # If the value in list2 is smaller, append it to the merged list
            '''merged list [1, 1]'''
            current.next = list2  # Append the current node of list2 to the merged list
            # Move to the next node in list2
            '''update pointers
               list1: [1] -> [2] -> [4] -> None
               list2: [3] -> [4] -> None '''
            list2 = list2.next  # Move the list2 pointer to the next node
        
        # Move the pointer to the next node in the merged list
        current = current.next

    # Append the remaining nodes of list1 or list2 to the merged list
    '''2nd Iteration:
       list1: [2] -> [4] -> None
       list2: [3] -> [4] -> None '''
    current.next = list1 if list1 else list2
    
    # Return the head of the merged list (excluding the dummy node)
    return dummy.next

# Create instances of the linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Call the mergeTwoLists function
merged_list = mergeTwoLists(list1, list2)

# Print the values of the merged list
while merged_list:
    print(merged_list.val, end=' ')
    merged_list = merged_list.next