function findModSum2 (data,a,b) {
    
    var suma = 0

    for (i = 0; i < data.lenght; i = i + 1) {

        if (data[i] > a && data[i] < b) {

            suma = suma + data[i]

        }

    }
    console.log(suma)

}
console.log(findModSum2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],7,14))
