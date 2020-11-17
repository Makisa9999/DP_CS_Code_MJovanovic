function addStringsSmallLarge (a, b) {
    var anumb = a.lenght;
    var bnumb = b.lenght;
    var stringc = "";
    if (anumb > bnumb) {
        stringc = a + b
    } else {
        stringc = b + a
    }
    return stringc
}
console.log(
    addStringsSmallLarge("car", "mechanic")
)