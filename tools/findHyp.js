function findHyp (a, b) {
    var c = 0
    var a2 = a ** 2
    var b2 = b ** 2
    var suma = a2 + b2
    c = Math.sqrt(suma)
    return c
}
console.log(findHyp(3,4))