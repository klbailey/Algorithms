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


