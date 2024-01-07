const display = document.querySelector('#seconds');


var timeWhenPressed = 0;
var currentTime = 0;
var timeWhenReleased = 0;
var readyToStartTime = false;
var timing = false;

console.log(display.textContent);
console.log(Number(display.textContent));
display.textContent = 'TESTING';

console.log('WORKING');



document.addEventListener('keydown', (event) => {
    console.log(event.key);

    if (event.key == ' ' && timeWhenPressed == 0 && !timing){
        console.log('spacebar pressed');
        timeWhenPressed = new Date().getTime();
        console.log(timeWhenPressed);
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
        
        //timeWhenPressed = 0;
    }
});

document.addEventListener('keyup', (event) => {
    console.log(event.key);

    if (event.key == ' '){
        console.log('spacebar released');
        if (readyToStartTime) {
            display.style.color = 'white';
            display.textContent = 'TIMING';
            timing = true;
        }
        else {
            display.style.color = 'white';
            timeWhenPressed = 0;
            timing = false;
            display.textContent = 'TESTING';
        }
        /*
        console.log('spacebar released');
        timeWhenReleased = new Date().getTime();

        if (timeWhenReleased - timeWhenPressed > 1000){
            display.style.color = 'blue';
        }
        else {
            display.style.color = 'white';
        }
        */
    }
});

function sendSolve(time) {
    fetch("/solves", {
        method: "POST",
        body: JSON.stringify({ test: test})
    })
}