function findModSum4 (d) {
    var suma = 0
    var a = ""
    var b = 0

    for (let i = 0; i < d.length(); i++) {
        a = toString(d[i])
        a = a.replace(".", "")
        for (let i = 0; i < a.length(); i++) {
            b = //to int a[i]
            suma = suma + b
        }
    }
    return suma
}