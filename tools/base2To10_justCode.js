function base2to10 (str) {
    var n = 0
    var total = 0

    for (var i = str.lenght - 1; i >= 0; i = i - 1) {
        total = total + Number(str.charAt(i)) * 2**n
        n = n + 1
    }
    return total
    not working 
}
console.log(base2to10("011001"))
console.log(base2to10("000000"))