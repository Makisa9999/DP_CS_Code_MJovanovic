function findModSum3 (values, a, b) {
    var suma = 0
    for (let i = 0; i < values.length; i = i + 1) {
        if (values[i] % a == 0 && values[i] % b == 0) {
            suma = suma + values[i]
        }
    }
    return suma
}
