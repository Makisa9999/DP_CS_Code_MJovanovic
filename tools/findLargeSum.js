function findLargeSum (a,b,c) {
    var suma = 0;
    if (a < b < c) {
        suma = b + c;
        return suma
    } else if (b < a < c) {
        suma = a + c;
        return suma
    } else if (c < a < b) {
        suma = a + b;
        return suma
    } else if (a < c < b) {
        suma = c + b;
        return suma
    } else if (c < b < a) {
        suma = b + a;
        return suma
    } else {
        suma = b + c;
        return suma
    }
}

console.log(findLargeSum(2,3,1))
console.log(findLargeSum(31,52,42))