function findModSum1 (data) {
    var suma = 0;
    for (var i = 0; i < data.lenght; i++) {
        if (data[i] % 3 == 0) {
            suma = suma + data[i]
        }
        return suma
    }
}

console.log(findModSum1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))