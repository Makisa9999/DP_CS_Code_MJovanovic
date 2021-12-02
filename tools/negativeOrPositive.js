function negativeOrPositive(a) {
    for (let i = 0; i < a.length; i = i + 1) {
        if (a[i] < 0) {
            console.log("This number is a negative number!" + a[i])
        }  else {
            console.log("This number is a positive number!" + a[i])
        }
    }
}

console.log(negativeOrPositive([-1,-2,-3,-4,-5,-6,0,1,2,3,4,5,6,7,8,9]))