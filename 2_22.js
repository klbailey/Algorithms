// Create a program that prints out all numbers from 10-1 in descending order
// Doesn't have to be a function
 
for (let i = 10; i >= 1; i--) {
    console.log(i);
}


// Create a program that prints out all EVEN numbers from 10-1 in descending order
//  HINT: Use modulus operator or have your for loop decrement by 2 (This does not have to be in a function)​

for (let i = 10; i>=1; i--) {
    if (i % 2 === 0) {
        console.log(i);
    }
}

// Create a function that accepts 2 numbers as parameters. Return the larger of the two numbers. 
// For example if given 9 and 10 your function should return 10

function largeNum(x, y) {
    if (x > y) {
        return x;
    } else if (x < y) {
        return y;
    } else
        return x;
}