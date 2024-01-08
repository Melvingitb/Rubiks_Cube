const scrambleDisplay = document.querySelector('#scramble');
const display = document.querySelector('#seconds');

var timeWhenPressed = 0;
var currentTime = 0;
var timeWhenReleased = 0;
var timeWhenStopped = 0;
var solveTime = 0;
var readyToStartTime = false;
var timing = false;
var interval;
var displayInterval;
var scramble = generateScramble();

scrambleDisplay.textContent = scramble;

document.addEventListener('keydown', (event) => {
    //console.log(event.key);

    if (event.key == ' ' && timeWhenPressed == 0 && !timing){
        //console.log('spacebar pressed');
        timeWhenPressed = new Date().getTime();
        //console.log(timeWhenPressed);
        display.style.color = 'red';
    }
    else if (event.key == ' ' && timeWhenPressed != 0 && !timing){
        currentTime = new Date().getTime();
        if (currentTime - timeWhenPressed > 250){
            display.style.color = 'green';
            readyToStartTime = true;
        }
    }
    else if (timing){
        //timing = false;
        readyToStartTime = false;
        display.style.color = 'red';
        clearInterval(interval);
        clearInterval(displayInterval);
        display.textContent = solveTime.toFixed(2);

        console.log(solveTime);
        console.log(scramble);
        
        sendSolve(solveTime, scramble);

        scramble = generateScramble();
        scrambleDisplay.textContent = scramble;
        //timeWhenPressed = 0;
    }
});

document.addEventListener('keyup', (event) => {
    //console.log(event.key);

    if (event.key == ' '){
        //console.log('spacebar released');
        if (readyToStartTime) {
            timeWhenReleased = new Date().getTime();
            display.style.color = 'white';
            //display.textContent = 'TIMING';
            timing = true;

            interval = setInterval(() => {
                currentTime = new Date().getTime();

                solveTime = (currentTime - timeWhenReleased) / 1000;
            }, 10);

            displayInterval = setInterval (() => {
                display.textContent = solveTime.toFixed(1);
            }, 100);
        }
        else {
            display.style.color = 'white';
            timeWhenPressed = 0;
            timing = false;
        }
    }
});

// generates a random legal scramble
function generateScramble() {
    let ret = '';
    let lastMove;
    let nextMove;
    let moves = ["R", "R\'", "R2", "L", "L\'", "L2", "U", "U\'", "U2", "B", "B\'", "B2", "F", "F\'", "F2", "D", "D\'", "D2"];

    // shuffle the moves, pop a move, add it to the scramble, then remove related moves from moves list
    shuffle(moves);
    lastMove = moves.pop();
    ret = ret.concat(lastMove, ' ');
    moves = validateMoves(lastMove, moves);

    //console.log(moves);
    //console.log(ret);

    for (let i = 0; i < 18; i++){

        shuffle(moves);
        nextMove = moves.pop();
        if (i == 18){
            ret = ret.concat(nextMove);
        }
        else {
            ret = ret.concat(nextMove, ' ');
            moves = validateMoves(nextMove, moves);
            moves = replaceMoves(lastMove, moves);

            lastMove = nextMove;
            
        }
    }
    //console.log(ret);
    return ret;
}

// puts all related moves back into the moves array
function replaceMoves(previousMove, movesArray) {
    let letter = previousMove.charAt(0);

    movesArray.push(letter);
    movesArray.push(letter.concat('2'));
    movesArray.push(letter.concat('\''));

    return movesArray;
}

// removes all related moves from the array
function validateMoves(previousMove, movesArray) {
    if (previousMove.slice(-1) == '\''){
        let letter = previousMove.charAt(0);

        let index = movesArray.indexOf(letter);
        movesArray.splice(index, 1);

        index = movesArray.indexOf(letter.concat('2'));
        movesArray.splice(index, 1);
    }
    else if (previousMove.slice(-1) == '2'){
        let letter = previousMove.charAt(0);

        let index = movesArray.indexOf(letter);
        movesArray.splice(index, 1);

        index = movesArray.indexOf(letter.concat('\''));
        movesArray.splice(index, 1);
    }
    else {
        let letter = previousMove.charAt(0);

        let index = movesArray.indexOf(letter.concat('2'));
        movesArray.splice(index, 1);

        index = movesArray.indexOf(letter.concat('\''));
        movesArray.splice(index, 1);
    }

    return movesArray;
}

// Fisher-Yates (aka Knuth) Shuffle
function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex > 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
}

function sendSolve(time, scramble) {
    fetch("/solves", {
        method: "POST",
        body: JSON.stringify({ time : time, scramble : scramble})
    })
}