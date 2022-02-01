// This is my encryption function that I can use to create encrypted messages that 
// are going to be used to store passwords and emails in the database.
let encryption = (function(){
    
    return{
        // Ecnryption function
        encryptMess: (mess = '', key = '') => {
            var encrypted = CryptoJS.AES.encrypt(mess, key);
            return encrypted.toString();
        },
        // Decryption function
        decryptMess: (mess = '', key = '') => {
            var decryptedBytes = CryptoJS.AES.decrypt(mess, key);
            var decryptedMessage = decryptedBytes.toString(CryptoJS.enc.Utf8);
            return decryptedMessage;
        }
    }
})();

// [Email, password, admin status]
userList = []
var decryptedUserList = []
database.ref("users/").once("value", (snapshot) => {
    userList = snapshot.val()
    decryptedUserList = decryptAccounts(userList)
});

// Active user and current user
var currentUser = []
var activeUser = ""

// Document Object Model - Getting all the objects for login function.
var login_email_1 = document.getElementById("login_email_1")
var login_password_1 = document.getElementById("login_password_1")
var incorrect_password_message = document.getElementById("incorrect_password_message")
var bannedWordsForm = document.getElementById("bannedWordsForm")
var badWordSubmit = document.getElementById("badWordSubmit")
var selectUser = document.getElementById("selectUser")

// Naming a function checkLogin - takes 0 parameters
function checkLogin () {
    // Getting the value of email field that user inputted
    var email = login_email_1.value
    // Getting the value of password field that user inputted
    var password = login_password_1.value
    // Loop thought all the users in the database.
    for (let key in userList) {
        // Get the email from the database by calling the variable and accessing the key and the "email" field and then decrypt it.
        var databaseEmail = encryption.decryptMess(userList[key]["email"], "your_email")
        // Get the password from the database by calling the variable and accessing the key and the "password" field and then decrypt it.
        var databasePassword = encryption.decryptMess(userList[key]["password"], "your_password")
        // Check if the database email and password are the same as the email and password entered by user.
        if ((databaseEmail === email) && (databasePassword === password)) {
            // Get the modal that is used to login.
            var elem = document.getElementById("loginToAccount");
            // Then this gets the component and all the data available
            var instance = M.Modal.getInstance(elem);
            // Close the modal
            instance.close();
            // This stops from incorrect password message showing
            incorrect_password_message.style.display = "none"
            // Set the currentUser list to empty.
            currentUser = []
            // Push the logged in user to the currentUser list
            currentUser.push(databaseEmail)
            // Set activeUser as current user at field 0
            activeUser = currentUser[0]
            // Set the variable to either 0 or 1 whether the user is admin.
            admin = userList[key]["admin"]
            // Run this function so it displayes only cards made by the logged in user.
            findProperties(data)
            // If the user is admin
            if (admin === 1) {
                // Allow the user to enter words to be banned
                bannedWordsForm.style.display = "block"
                // Allow the user to see the submit button for banned words
                badWordSubmit.style.display = "block"
                // Run the function where the admin is going to get all the users and will be able to see their cards.
                setupSelect()
            // if the user is not admin
            } else if (admin === 0) {
                // Don't allow the user to see the form to submit banned words
                bannedWordsForm.style.display = "none"
                // Don't allow the user to see the sumbit button to the banned words form
                badWordSubmit.style.display = "none"
            }
        // if the user information is incorrect
        } else {
            // Display message that it is incorrect. 
            incorrect_password_message.style.display = "block"
        }

    }
}

const selectAdmin = document.getElementById("adminDropdown")
const adminCommand = document.getElementById("adminCommand")

function setupSelect () {
    adminCommand.style.display = "block"
    var divSelectAdmin = ""
    for (let key in userList) {
        var decryptedEmail = encryption.decryptMess(userList[key]["email"], "your_email")
        var htmlText = `<li><a href="#!" onclick="displayUser('${decryptedEmail}')">${decryptedEmail}</a></li>`
        divSelectAdmin = divSelectAdmin + htmlText
    }
    selectAdmin.innerHTML = divSelectAdmin
}

const adminDiv = document.getElementById("adminDiv")

function displayUser(displayedUser) {
    console.log(displayedUser)
    var finishedDiv = ""
    // Code the function so it adds to inner html cards that the pressed user has. 
    for (let key in data) {
        if (data[key]["user"] === displayedUser) {
            var newCard = createCard(data[key]["id"], data[key]["subject"], data[key]["dueDate"], data[key]["color"], data[key]["description"])
            finishedDiv = finishedDiv + newCard
        }
    }
    adminDiv.innerHTML = finishedDiv
}

// Getting elements for register. Register function.
var register_email_1 = document.getElementById("register_email_1")
var register_email_2 = document.getElementById("register_email_2")
var register_password_1 = document.getElementById("register_password_1")
var register_password_2 = document.getElementById("register_password_2")
var register_wrong_entry = document.getElementById("wrong_input_message")
var user_exists_message = document.getElementById("user_exists_message")
var less_than_6_message = document.getElementById("less_than_6_message")
var capital_letter_message = document.getElementById("capital_letter_message")
var has_digit_message = document.getElementById("has_digit_message")

function checkRegister () {
    var email_1 = register_email_1.value
    var email_2 = register_email_2.value
    var password_1 = register_password_1.value
    var password_2 = register_password_2.value
    var flag = false
    if (email_1 != "" || password_1 != "") {
        for (let i = 0; i < userList.length; i = i + 1) {
            if (userList[i]["email"] === email_1) {
                register_wrong_entry.style.display = "none"
                user_exists_message.style.display = "block"
                flag = true
                console.log("User Exists!")
            }
        }
        if (password_1.length < 6 || password_2.length < 6) {
            // Display a message that will tell the user that their password is less than 6 characters.
            less_than_6_message.style.display = "block"
            capital_letter_message.style.display = "none"
            has_digit_message.style.display = "none"
            register_wrong_entry.style.display = "none";
            user_exists_message.style.display = "none"
        } else if (password_1.search(/[A-Z]/) < 0) {
            // Display a message that will tell the user that their password needs a capital letter.
            less_than_6_message.style.display = "none"
            capital_letter_message.style.display = "block"
            has_digit_message.style.display = "none"
            register_wrong_entry.style.display = "none";
            user_exists_message.style.display = "none"
        } else if (password_1.search(/[0-9]/) < 0) {
            // Display a message that will tell the user that their password needs a number. 
            less_than_6_message.style.display = "none"
            capital_letter_message.style.display = "none"
            has_digit_message.style.display = "block"
            register_wrong_entry.style.display = "none";
            user_exists_message.style.display = "none"
        } else {
            // Proceed
            if ((email_1 == email_2) && (password_1 == password_2) && (flag === false)) {
                register_wrong_entry.style.display = "none";
                user_exists_message.style.display = "none"
                less_than_6_message.style.display = "none"
                capital_letter_message.style.display = "none"
                has_digit_message.style.display = "none"
                var elem = document.getElementById("createAccount");
                var instance = M.Modal.getInstance(elem);
                instance.close();
                var temporary = {"email": encryption.encryptMess(email_1, "your_email"), "password": encryption.encryptMess(password_1, "your_password"), "admin": 0}
                return temporary
            } else {
                register_wrong_entry.style.display = "block";
                user_exists_message.style.display = "none"
                less_than_6_message.style.display = "none"
                capital_letter_message.style.display = "none"
                has_digit_message.style.display = "none"
                return "Invalid Input"
            }
        }
    }
}

// Reset all fields
function resetAllFields () {
    login_email_1.value = "";
    login_password_1.value = "";
    register_email_1.value = "";
    register_email_2.value = "";
    register_password_1.value = "";
    register_password_2.value = "";
}

//Make a function that will hide my account and homework tabs.
const welcomePage = document.getElementById("welcomePage") // if active user = "" display: block; activeuser = soemthing display:none;
const loggedInDiv = document.getElementById("loggedInDiv") // if activeuser = something display: block; if active user = "" display: none;
const loginLinks2 = document.getElementById("loginLinks2") // if active user = "" display: none; if activeuser = something display: block;
const loginLinks3 = document.getElementById("loginLinks3") // if active user = "" display: none; if activeuser = something display: block;
const logoutLinks = document.getElementById("logoutLinks") // if active user = "" display: block; if activeuser = something display: none;
const background_image = document.getElementById("background-image")
const adminOnly = document.getElementById("adminOnly")

function checkIfLoggedIn () {
    if (activeUser != "" && activeUser != "admin@admin.com") {
        welcomePage.style.display = "none"
        adminDiv.style.display = "none"
        adminCommand.style.display = "none"
        loggedInDiv.style.display = "block"
        loginLinks2.style.display = "block"
        loginLinks3.style.display = "block"
        logoutLinks.style.display = "none"
        background_image.style.display = "none"
        adminOnly.style.display = "none"
    } else if (activeUser == "") {
        welcomePage.style.display = "block"
        adminDiv.style.display = "none"
        adminCommand.style.display = "none"
        loggedInDiv.style.display = "none"
        loginLinks2.style.display = "none"
        loginLinks3.style.display = "none"
        logoutLinks.style.display = "block"
        background_image.style.display = "block"
        adminOnly.style.display = "none"
    } else if (activeUser == "admin@admin.com") {
        welcomePage.style.display = "none"
        adminDiv.style.display = "block"
        adminCommand.style.display = "block"
        loginLinks2.style.display = "block"
        loginLinks3.style.display = "block"
        logoutLinks.style.display = "none"
        background_image.style.display = "none"
        adminOnly.style.display = "block"
    }
}



// 6 lines below are used for login system to work.
const loginButton = document.getElementById("loginAccount")
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    checkLogin();
    resetAllFields();
    checkIfLoggedIn();
});

// 5 lines below are used for cancel button for login modal.
const loginCancel = document.getElementById("loginCancel")
loginCancel.addEventListener("click", (e) => {
    e.preventDefault();
    resetAllFields();
    checkIfLoggedIn();
})

// 6 lines below are used for register system to work.
const registerButton = document.getElementById("registerAccount")
registerButton.addEventListener("click", (e) => {
    e.preventDefault();
    registerUserInDatabase();
    resetAllFields();
    checkIfLoggedIn();
});

// 5 lines below are used for cancel button for register modal.
const registerCancel = document.getElementById("registerCancel")
registerCancel.addEventListener("click", (e) => {
    e.preventDefault();
    resetAllFields();
    checkIfLoggedIn();
})

// 11 lines below are used by the cancel button for new cards modal to delete all inputs in the fields. 
const subjectInput = document.getElementById("subjectInput")
const dueDateInput = document.getElementById("dueDateInput")
const descriptionInput = document.getElementById("descriptionInput")
const colorInput = document.getElementById("colorInput")
const cancelCreateNewCardButton = document.getElementById("cancelCreateNewCardButton")
cancelCreateNewCardButton.addEventListener("click", (e) => {
    e.preventDefault();
    subjectInput.value = ""
    dueDateInput.value = ""
    descriptionInput.value = ""
    colorInput.value = ""
});

var data = []

function createCard(id, subject, dueDate, color, description) {
    var card = `<div class="col s12 m6">
                    <div class="card ${color}">
                        <div class="card-content white-text">
                            <span class="card-title center">${subject}</span>
                            <div style="border:1px solid white;padding: 0px 2px 0px 2px;">
                                <p>Due Date: ${dueDate}</p>
                            </div>
                            <div style="border:1px solid white;padding:2px;">
                                <p>Description: <br />${description}</p>
                            </div>
                        </div>
                        <div class="card-action center">
                            <a class="btn removeButton" href="#" id="removeButton${id}" onclick="removeElementFromDatabase(this.id)">REMOVE CARD</a>
                        </div>
                    </div>
                </div>`
    return card
}

// Trying to make a function that when remove button is clicked it will get the ID 
// of the button and then it is going to get the last two numbers of the id of the button
// which is the id of the element that is in the database. Then you are going to access
// the parent that is in the database and remove it.

function getTheElementId (strings) {
    // This line will get the string which is the ID of the button, then since the ID for 
    // each element in the database is proportional to the ID of the button since it is in
    // the form removeButton + ID in the database. The part of the line .match(/\d/g) will 
    // rip out everything that is a letter out of the string which will leave only numbers 
    // in the string and then it would join every number together and tranfer it into an 
    // interger and return it. 
    numb = Number(strings.match(/\d/g).join(""));
    return numb
}

// Write a function that removes the card
function removeCard (a) {
    var x = document.getElementById(a)
    var y = x.parentElement.parentElement.parentElement
    y.remove()
}

const cardDiv = document.getElementById("cardDiv")
function findProperties(data) {
    fullDiv = ""
    for (let i in data) {
        var id = data[i]["id"]
        var subject = data[i]["subject"]
        var dueDate = data[i]["dueDate"]
        var color = data[i]["color"]
        var description = data[i]["description"]
        newCard = createCard(id, subject, dueDate, color, description)
        aU = activeUser
        userFromCard = data[i]["user"]
        if (userFromCard == aU) {
            var fullDiv = fullDiv + newCard
        } else if (aU === "admin@admin.com") {
            var fullDiv = fullDiv + newCard
        }
    }
    cardDiv.innerHTML = fullDiv
}

data = []

// Next thing to make is that when you click to remove a card the page is not going to scroll to the top. 

//-----------------------------------------------------------------------------------------------

// DATABASE STUFF

// Pulling the users from the database
database.ref("users/").on("value", (snapshot) => {
    userList = snapshot.val()
    decryptedUserList = decryptAccounts(snapshot.val())
})

function decryptAccounts (listOfUsers) {
    for (let i = 0; i <= listOfUsers.length; i = i + 1) {
        for (let key in listOfUsers[i]) {
            if (key === "email") {
                listOfUsers[i][key] = encryption.decryptMess(listOfUsers[i][key], "your_email")
            } else if (key === "password") {
                listOfUsers[i][key] = encryption.decryptMess(listOfUsers[i][key], "your_password")
            }
        }
    }
    return listOfUsers
}

var data = null
//Pulling cards from the database
var cards = database.ref("cards/").on("value", (snapshot) => {
    const cardsLst = snapshot.val();
    data = cardsLst
    findProperties(data)
})
var bannedWordsLst
//Pulling banned words from the database
var bannedWords = database.ref("bannedWords/").on("value", (snapshot) => {
    bannedWordsLst = snapshot.val();
});

//We are making that when you submit a form, information would be gathered and then it is going to be pushed to the database.
var submitCreateNewCardButton = document.getElementById("submitCreateNewCardButton")
const badWordMessage = document.getElementById("badWordMessage")
submitCreateNewCardButton.addEventListener("click", (e) => {
    e.preventDefault();
    var subject = subjectInput.value;
    var dueDate = dueDateInput.value;
    var description = descriptionInput.value;
    var color = colorInput.value;
    subjectInput.value = "";
    dueDateInput.value = "";
    descriptionInput.value = "";
    colorInput.value = "";
    var id = cardDiv.children.length;
    var result = checkForBadWordsOnCards(subject, dueDate, description, color)
    if (result == false) {
        badWordMessage.style.display = "none"
        database.ref("cards/").push({
            "subject": subject,
            "dueDate": dueDate,
            "description": description,
            "color": color,
            "id": id,
            "user": activeUser
        });
    } else {
        badWordMessage.style.display = "block"
    }
});

function removeElementFromDatabase(buttonId) {
    var idDatabase = getTheElementId(buttonId)
    // Loop through the database and then you can find the ID of the element you are
    // trying to delete and then you would get the parent id and delete the whole entry 
    // in the database.
    for (let key in data) {
        if (data[key]["id"] === idDatabase) {
            delete data[key]
        }
    }
    database.ref("cards/").set(data)
}

function registerUserInDatabase () {
    // Get values for everysingle field in the register form. then check if they are all 
    // the same push it to users and then take users and push it into the database so it 
    // updates and creates a new id.
    var a = checkRegister()
    database.ref("users/").push(a)
}

function logout() {
    activeUser = ""
    checkIfLoggedIn()
    console.log("Logged Out!")
    adminDiv.innerHTML = ""
}

document.getElementById("loginLinks3").addEventListener("click", (e) => {
    e.preventDefault()
    logout()
})

const curseWordInput = document.getElementById("curseWordInput")

badWordSubmit.addEventListener("click", (e) => {
    e.preventDefault()
    var word = curseWordInput.value
    database.ref("bannedWords/").push(word)
    curseWordInput.value = ""
})

function checkForBadWordsOnCards(subject, dueDate, description, color) {
    var flagForBadWords = false
    for (let key in bannedWordsLst) {
        badWord = bannedWordsLst[key]
        subjectTemp = subject.includes(badWord)
        dueDateTemp = dueDate.includes(badWord)
        descriptionTemp = description.includes(badWord)
        colorTemp = color.includes(badWord)
        if (subjectTemp != false || dueDateTemp != false || descriptionTemp != false || colorTemp != false) {
            flagForBadWords = true
            return flagForBadWords
        } else {
            flagForBadWords = false
        }
    }
    return flagForBadWords
}

function adminViewAdmin () {
    adminDiv.style.display = "block"
    loggedInDiv.style.display = "none"
}

function userViewAdmin () {
    adminDiv.style.display = "none"
    loggedInDiv.style.display = "block"
}