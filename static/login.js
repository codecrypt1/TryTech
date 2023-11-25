const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
// const signInSuccess = document.getElementById('signedIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

document.addEventListener('DOMContentLoaded', function() {
    var signInButton = document.getElementById('signedIn');


    signInButton.addEventListener('click', function(event) {
        // Prevent default form submission
        event.preventDefault();

        // Redirect to a new page
        window.location.href = 'C:/Users/Kriz/Desktop/Dora/Dora/user_page.html'; // Replace with your desired URL
        console.log("Welcomeee")
    });
});

