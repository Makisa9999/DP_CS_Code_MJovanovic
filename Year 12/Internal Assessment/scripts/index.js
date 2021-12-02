// [Email, password, admin status]
var users = []
// Active user and current user
var currentUser = []
var activeUser = ""

// Getting Elements for login. Login Function
var login_email_1 = document.getElementById("login_email_1")
var login_password_1 = document.getElementById("login_password_1")
function checkLogin () {
    var email = login_email_1.value
    var password = login_password_1.value
    for (let i = 0; i < users.length; i++) {
        if ((users[i]["email"] === email) && (users[i]["password"] == password)) {
            console.log("Successful login!")
            currentUser.push(email)
            activeUser = currentUser[0]
        }
    }
}



// Getting elements for register. Register function.
var register_email_1 = document.getElementById("register_email_1")
var register_email_2 = document.getElementById("register_email_2")
var register_password_1 = document.getElementById("register_password_1")
var register_password_2 = document.getElementById("register_password_2")
var register_wrong_entry = document.getElementById("wrong_input_message")
function checkRegister () {
    var email_1 = register_email_1.value
    var email_2 = register_email_2.value
    var password_1 = register_password_1.value
    var password_2 = register_password_2.value
    var flag = false

    for (let i = 0; i < users.length; i++) {
        // if user exists dont add/
        if ((users[i][0] === email_1) && (users[i][0] === email_2)) {
            register_wrong_entry.style.display = "none";
            console.log("User already exists!");
            flag = true;
            console.log(users)
        }
    }

    if ((email_1 == email_2) && (password_1 == password_2) && (flag === false)) {
        register_wrong_entry.style.display = "none";
        var temporary = [email_1, password_1, 0]
        users.push(temporary)
        console.log(users)
    } else {
        register_wrong_entry.style.display = "block";
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



// 6 lines below are used for login system to work.
const loginButton = document.getElementById("loginAccount")
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    checkLogin();
    resetAllFields();
});

// 5 lines below are used for cancel button for login modal.
const loginCancel = document.getElementById("loginCancel")
loginCancel.addEventListener("click", (e) => {
    e.preventDefault();
    resetAllFields();
})

// 6 lines below are used for register system to work.
const registerButton = document.getElementById("registerAccount")
registerButton.addEventListener("click", (e) => {
    e.preventDefault();
    checkRegister();
    resetAllFields();
});

// 5 lines below are used for cancel button for register modal.
const registerCancel = document.getElementById("registerCancel")
registerCancel.addEventListener("click", (e) => {
    e.preventDefault();
    resetAllFields();
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
                            <span class="card-subtitle center">${dueDate}</span>
                            <p>${description}</p>
                        </div>
                        <div class="card-action center">
                            <a class="btn removeButton" href="#" id="removeButton${id}" onclick="removeCard(this.id)">REMOVE CARD</a>
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
    temporaryList = []
    for (let i = 0; i < strings.length; i++) {
        temporaryList.push(strings[i])
    }
    for (let j = 0; j < temporaryList.length; j++) {
        temporaryList.shift()
        console.log(temporaryList)
    }
}

function removeElementFromDatabase (id) {
    var id = "removeButton0"
    
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
        var newCard = createCard(id, subject, dueDate, color, description)
        var fullDiv = fullDiv + newCard
    }
    cardDiv.innerHTML = fullDiv
}

var data = []

// Next thing to make is that when you click to remove a card the page is not going to scroll to the top. 

//-----------------------------------------------------------------------------------------------

// DATABASE STUFF

// Pulling the users from the database
var users = database.ref("users/").on("value", (snapshot) => {
    const usersLst = snapshot.val();
    users = usersLst
});

//Pulling cards from the database
var cards = database.ref("cards/").on("value", (snapshot) => {
    const cardsLst = snapshot.val();
    data = cardsLst
    findProperties(data)
})

//Pulling banned words from the database
var bannedWords = database.ref("bannedWords/").on("value", (snapshot) => {
    const bannedWordsLst = snapshot.val();

});

//We are making that when you submit a form, information would be gathered and then it is going to be pushed to the database.
var submitCreateNewCardButton = document.getElementById("submitCreateNewCardButton")
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
    var cardPush = database.ref("cards/").push({
        "subject": subject,
        "dueDate": dueDate,
        "description": description,
        "color": color,
        "id": id
    });
});
