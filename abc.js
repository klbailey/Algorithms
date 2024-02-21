// Create a function that accepts 2 parameters x and y. This function should print out the 
// product of both numbers (x * y), the quotient of both numbers (x/y), the sum of both numbers (x + y), 
// and the difference of both numbers (x-y).​

function twoNumbers ( x, y) {
    console.log(x * y)
    console.log(x / y)
    console.log(x + y)
    console.log(x-y)
}

// Create a function that accepts a number parameter and returns the sum of all of the numbers from 0 to that number. 
// For example if given 5 return ( 0 + 1 + 2 + 3 + 4 + 5) or 15.

function someNumber (num) {
    // initialize a variable to store a sum that starts as 0
    let sum = 0;
    //  for loop iterates from 0 to the given number
    for (let i = 0; i <= num; i++) {
        // add current value of i to sum
        sum += i;
    }
    // return sum
    return sum;
}