const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


// for disappear error message itself
setTimeout(function() {
    $('#message').fadeOut('slow');
  }, 3000);