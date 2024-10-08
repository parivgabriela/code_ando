function startTimer(duration, progressBar) {
    var timer = duration, minutes, seconds;
    var interval = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        // display.textContent = minutes + ":" + seconds;

        var percentage = ((duration - timer) / duration) * 100;
                progressBar.style.width = 100 - percentage + "%";
        
        // Change color to red when timer reaches 10 seconds
        if (timer <= 10) {
            //display.classList.add("red");
            progressBar.classList.add("red");
        }

        if (--timer < 0) {
            clearInterval(interval);
        }
        if (--timer < 0) {
            clearInterval(interval);
            // Redirect to time-up page when the timer reaches zero
            window.location.href = "/time_up";
        }
    }, 1000);
}

window.onload = function () {
    var oneMinute = 60,
        //display = document.querySelector('#timer');
        progressBar = document.querySelector('#progress-bar');
    startTimer(oneMinute, progressBar);
};

