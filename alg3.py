'''Intermediate Sums You will be given an array of numbes. After every tenth element, add
an additional element containing the sum of those 10 values. If the array doesn't end aligned 
evenly w/10 elements, add 1 last sum that includes those last elements not yet been included
in one of the earlier sums.  
Given the array [1,2,1,2,1,2,1,2,1,2,1,2,1,2], 
change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6].
'''
def intermediate_sums(arr):
    result = [] #empty list to store intermediate sums 
    current_sum = 0 #keep track of sum of current 10 eements
    # The enumerate() function is used to iterate over the elements of arr along with their indices
    # i will be index of current element and num is value of current element
    for i, num in enumerate(arr):
        current_sum += num #adds num to current_sum accululates sum of current 10 elements
        if (i + 1) % 10 == 0: #checks if current indiex i+1 is multiple of 10
            result.append(current_sum) #if^^true adds curent_sum to result list
            current_sum = 0 #start calculating next 10 elements reset to 0
        elif i == len(arr) - 1:  # If it's the last element in arr
            result.append(current_sum) #add currrent_sum to result list

    return result

arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
sums = intermediate_sums(arr)

# Adjust the original array
for i in range(len(sums)): #loop over indices of sums list that contains intermediate sums
    index = (i + 1) * 10 + i #calc index current intermediate sum should be inserted (every 10)
    arr.insert(index, sums[i]) #inserts current intermediate sum sums[i] into orig arr at calc index

print(arr)

'''Instructor solution:'''

def intermediateSums(arr):
    count = 10
    sum_val = 0
    i = 0

    while i < len(arr):
        if count == 0:
            arr.insert(i, sum_val)
            count = 10
            sum_val = 0
        else:
            sum_val += arr[i]
            count -= 1

        i+=1

    if count >= 0:
        arr.append(sum_val)

    return arr

print(intermediateSums([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]))