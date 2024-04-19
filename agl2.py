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

def book_index(arr):
    pages = ""

    i = 0
    while i  < len(arr):
        pages += str(arr[i])
        currentIndex = i

        while i + 1 < len(arr) and arr[i+1] == arr[i] + 1:
            i+=1

        if i > currentIndex:
            pages += f"-{arr[i]}"

        if i + 1 < len(arr):
            pages += ","

        i+=1

    return pages


print(book_index([1,2,3,13,14,15,16,37,38,39,70]))

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

