function findIntervalSum (a, b) {
    var minimum = a;
    var maximum = b;
    var suma = 0;
    if (a < b) {
        for (let i = minimum; i < b + 1; i = i + 1) {
            suma = suma + i;
        }
        return suma;
    } else {
        for (let i = minimum; i < b + 1; i = i + 1) {
            suma = suma + i;
        }
        return suma;
    }
}

console.log(findIntervalSum(12,15))
console.log(findIntervalSum(1,3))