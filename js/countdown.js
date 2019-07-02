// Set the date we're counting down to
var countDownDate = new Date()
countDownDate.setSeconds(countDownDate.getSeconds() + 30)
countDownDate = countDownDate.getTime();

// Select the element we're displaying the countdown in
var countdown = document.getElementById("countdown");

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  countdown.textContent = seconds;

  // If the count is reaching its end, add some colour to it
  if (seconds < 10) {
     countdown.className = "calltoaction bold";
  }

  // If the count down is finished, reload page
  if (distance < 0) {
    clearInterval(x);
    location.reload(true);
  }
}, 1000);
