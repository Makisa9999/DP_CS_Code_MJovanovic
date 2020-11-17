function findAbsoluteDifference (a,b) {
    var suma = 0;
    if (a < b) {
        suma = b - a;
        return suma;
    } else {
        suma = a - b;
        return suma;
    }
}
console.log(findAbsoluteDifference(3,6))