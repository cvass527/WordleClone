
export class Wordle {
    constructor(wordToGuess) {
        this.round = 1;
        this.word = wordToGuess.toUpperCase();
        this.board = this.initBoard();
        this.keyboard = this.initKeyboard();
    }

    initBoard() {
        const board = [];
        for (let i = 0; i < 6; i++) {
            const row = [];
            for (let j = 0; j < 5; j++) {
                row.push(new LetterGuess('-','Placeholder'));
            }
            board.push(row);
        }
        return board;
    }

    initKeyboard(){
        const keys = [['Q','W','E','R','T','Y','U','I','O','P'],
                          ['A','S','D','F','G','H','J','K','L'],
                          ['Z','X','C','V','B','N','M']]
        const keyboard = []
        for(let i = 0; i < 3; i++){
            let keyboardRow = []
            for(let j = 0; j < keys[i].length; j++){
                keyboardRow.push(new LetterGuess(keys[i][j],'Placeholder'))
            }
            keyboard.push(keyboardRow)
        }
        return keyboard;
    }


    guessSubmission(userGuess){
        const result = this.checkGuess(userGuess)
        this.updateBoard(result)
        this.handleGameState(result)
    }

    handleGameState(guessResult)
    {
        const letters = []
        for (let i =0 ; i < 5; i++)
        {
            letters.push(guessResult[i].character)
        }

        const justWord = letters.join('')



        if (justWord === this.word) {
          window.location.href = '/won';
          return 'win';
        } else if (this.round > 6) {
          window.location.href = '/lost';
          return 'lose';
        }
        return 'ongoing';
    }

    updateBoard(userGuess) {
        // Update current row
        this.board[this.round - 1] = userGuess;
        this.round++;
    }

    updateKeyboard(myChar, newState)
    {
        for(let i = 0; i < 3; i++)
        {
            for(let j = 0; j < this.keyboard[i].length; j++)
            {
                if(myChar == this.keyboard[i][j].character)
                {
                    this.keyboard[i][j].state = newState
                    return true
                }
            }
        }
    }

    checkGuess(userGuess) {
        const guess = userGuess.toUpperCase();
        const result = [];

        for (let i = 0; i < 5; i++) {
          const currentChar = guess[i];

          if (currentChar === this.word[i]) {

            result.push(new LetterGuess(currentChar, 'Correct'));
            this.updateKeyboard(currentChar,'Correct')

          }
          else if (this.word.includes(currentChar)) {

            result.push(new LetterGuess(currentChar, 'IW'));
            this.updateKeyboard(currentChar,'IW')

          }
          else {

            result.push(new LetterGuess(currentChar, 'NIW'));
            this.updateKeyboard(currentChar,'NIW')
          }
        }

        return result;
    }


}

class LetterGuess{

    //states: Placeholder, Correct, NIW, IW

    constructor(character, state){
        this.character = character
        this.state = state
    }
}
