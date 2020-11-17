function findCircleArea (a) {
    if (a < 0) {
        return -1;
    } else {
        var pi = 3.14159
        var asqrd = a ** 2
        var total = 0
        total = asqrd * pi
        return total.toFixed(5)
    }
}
console.log(findCircleArea(-12))
console.log(findCircleArea(3))

