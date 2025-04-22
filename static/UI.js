// Add at the VERY TOP of UI.js
console.log("UI.js loaded!");

import { Wordle } from './WordleLogic.js';

// main.js
let game;  // A variable to hold the Wordle game instance

document.addEventListener('DOMContentLoaded', function() {

    fetch('/word')
        .then(response => response.json())
        .then(data => {
            console.log("Fetched word:", data.word);
            game = new Wordle(data.word);  // Instantiate with the actual word
            console.log("Game initialized:", game);
            updateBoardDisplay(game.board);
            updateKeyboardDisplay(game.keyboard);
        });

    // Set up your form handler here as in the previous answer
    const form = document.getElementById('guess-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Stop form from submitting normally

        // Get the value from the input field
        const guessInput = document.getElementById('guess');
        const guess = guessInput.value;

        game.guessSubmission(guess); // Call your JavaScript function

        updateBoardDisplay(game.board)
        updateKeyboardDisplay(game.keyboard)
        guessInput.value = ''; // Optionally clear the input
    });
});


function updateBoardDisplay(board) {
    // board: 2D array, e.g. [['A', '-', '-', '-', '-'], ...]
    const gridDiv = document.getElementById('grid');
    gridDiv.innerHTML = ''; // Clear previous content

    for (let row of board) {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'row';
        for (let tile of row) {
            const tileDiv = document.createElement('div');
            tileDiv.className = 'tile ' + tile.state.toLowerCase();


            tileDiv.textContent = tile.character;
            rowDiv.appendChild(tileDiv);
        }
        gridDiv.appendChild(rowDiv);
    }
}

function updateKeyboardDisplay(keyboard) {
    // keyboard: 2D array, e.g. [['A', '-', '-', '-', '-'], ...]
    const gridDiv = document.getElementById('keyboard');
    gridDiv.innerHTML = ''; // Clear previous content

    for (let row of keyboard) {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'row';
        for (let tile of row) {
            const tileDiv = document.createElement('div');
            tileDiv.className = 'tile ' + tile.state.toLowerCase();


            tileDiv.textContent = tile.character;
            rowDiv.appendChild(tileDiv);
        }
        gridDiv.appendChild(rowDiv);
    }
}


