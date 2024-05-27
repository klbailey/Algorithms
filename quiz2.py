

'''Array Shuffle: Create a function called shuffle(arr), to efficiently shuffle a given array’s 
values in random order. Hint: Remember the swap method? Use a random number generator to come up 
index that needs to be swapped. [1,2,3] => [2,1,3], [3,1,2]​'''

import random

def shuffle(arr):
    n = len(arr)
    for i in range(n):
        # Generate a random index to swap with
        j = random.randint(i, n - 1)
        # Swap the current element with the randomly chosen element
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# Example usage:
original_array = [1, 2, 3]
shuffled_array = shuffle(original_array)
print(shuffled_array)



''' Array: Filter Range. Given arr and values min and max, retain only the array values between 
min and max indexes. Given [1,2,3,4,5],2,4 return [3,4,5].No built-in array functions. This does 
not have to be done in place meaning you don't have to return the same array that was passed in as a parameter.'''



''' Create a standalone function that accepts an input string,removes leading and trailing white 
spaces (at beginning and end only) from the string and capitalizes the first letter of every word, 
and return that string. ​'''



'''Given a string of words (sentence) create a function that capitalizes every word in the string. 
Given “hello there skillspire” return “Hello There Skillspire”. Remember don’t use any built in methods 
to complete this task except any methods that capitalize a character. Remember don’t use any built in 
methods to complete this task except any methods that capitalize a character.​'''



'''Acronyms. Create a function that, given a string, returns the string’s acronym (first letters only, 
capitalized). Given "there's no free lunch gotta pay yer way", return "TNFLGPYW". Given "Live from New 
York it's Saturday Night", return "LFNYISN".'''

def acronym(string):
    words = string.split()
    acr = ''
    for word in words:
        acr += word[0].upper()
    return acr

print(acronym("Live from New York it's Saturday Night"))

'''Remove Shorter Strings. Given a string array and value (length), remove any strings shorter than 
length from the array. Given ([“you”,”I”,”ab”], 3) return [“you”]. You can use any functions that you 
have created. Hint use removeAt() or find a method that removes a value from an array'''

