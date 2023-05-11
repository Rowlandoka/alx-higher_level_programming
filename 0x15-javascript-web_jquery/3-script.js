// add a class 'red' on click
$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    $('header').addClass('red');
  });
});
