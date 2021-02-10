/* Script that adds the class red to the HTML tag HEADER when the user
clicks on the tag DIV#red_header */
$('#red_header').click(function () { // run when the DOM is ready
  $('header').addClass('red'); // add the class to the clicked element
});
