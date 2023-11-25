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

let glist = []
let blist = []

document.addEventListener('DOMContentLoaded', function() {
    var badHabitInput = document.getElementById('badHabitInput');
    var goodHabitInput = document.getElementById('goodHabitInput');
    var badHabitsList = document.getElementById('badHabitsList');
    var goodHabitsList = document.getElementById('goodHabitsList');
    var g_para = document.getElementById('gpara');
    var b_para = document.getElementById('bpara');
    
    function updateBadHabits() {
        b_para.value = blist.join(', '); // Join the array elements with a comma (or any separator you prefer)
    }

    document.getElementById('addBad').addEventListener('click', function(event) {
        event.preventDefault();
        var inputValue = badHabitInput.value.trim();
        if (inputValue !== '') {
            var listItem = document.createElement('li');
            listItem.textContent = inputValue;
            badHabitsList.appendChild(listItem);
            blist.push(inputValue)
            console.log(blist)
            badHabitInput.value = ''; // Clear the input field
            updateBadHabits();
        }
    });

    function updateGoodHabits() {
        g_para.value = glist.join(', '); // Join the array elements with a comma (or any separator you prefer)
    }



    document.getElementById('addGood').addEventListener('click', function(event) {
        event.preventDefault();
        var inputValue = goodHabitInput.value.trim();
        if (inputValue !== '') {
            var listItem = document.createElement('li');
            listItem.textContent = inputValue;
            goodHabitsList.appendChild(listItem);
            glist.push(inputValue)
            console.log(glist)
            goodHabitInput.value = ''; // Clear the input field
            updateGoodHabits();
        }
    });
});


// // var b_para = document.getElementById('bpara');
// g_para.textContent = glist
// console.log(g_para.textContent) 




