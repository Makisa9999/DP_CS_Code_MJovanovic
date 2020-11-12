var userNames = ["mario.jovanovic", "nenad.jovanovic", "ema.jovanovic", "suzana.jovanovic"]
var passWords = ["mario1234567890", "nenad1234567890", "ema1234567890", "suzana1234567890"]
let val = false

function checkLogin (user, password) {

    for (i = 0; i < userNames.length; i = i + 1) {
        if (userNames[i] === user) {
            if (passWords[i] === password) {
                val = true;
            }
        }
    }
    return val
}

function loginA (user, password) {
    if (checkLogin() === true) {
        window.location.href = "personal.html";
    }
}

loginA("mario.jovanovic", "mario1234567890")