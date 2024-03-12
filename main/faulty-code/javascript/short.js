let userData = []; // Stores the fetched user data

// Fetch user data from the API
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
  users.forEach(user => {
    let userDiv = document.createElement('div');
    userDiv.innerHTML = `Name: ${user.name}, Email: ${user.email}`;
    usersContainer.appendChild(userDiv);
  });
}

getUserData();
