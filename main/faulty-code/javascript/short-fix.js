let userData = []; // Stores the fetched user data

//Fetch user data from the API
function getUserData() {
fetch('https://jsonplaceholder.typicode.com/users')
.then((response) => response.json())
.then((data) => {
userData = data;
displayUsers(data);
})
.catch((error) => console.log('Error:', error));
}

// Display users on the page
function displayUsers(users) {
let usersContainer = document.getElementById('users');
usersContainer.innerHTML = ''; // Clear the users container

// Separate concerns by creating a function to generate user div
function createUserDiv(user) {
let userDiv = document.createElement('div');
userDiv.innerHTML = `Name: ${user.name}, Email: ${user.email}`;
return userDiv;
}

// Use map instead of forEach for better readability
const userDivs = users.map(user => createUserDiv(user));

// Append all user divs to the users container at once for better performance
userDivs.forEach(userDiv => usersContainer.appendChild(userDiv));
}

getUserData();

//Adjustment-counter: 3
