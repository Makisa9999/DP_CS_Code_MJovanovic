function allEven (n) {
    var even = true;
    while (n > 0 && even == true) {
        if ((n % 10) % 2 == 1) {
            even = false
        }
        n = Math.floor(n/10)
        console.log(n)
        return even
    }
}
console.log(allEven (345))
console.log(allEven (236))
