$(document).foundation({
    offcanvas : {
        // Should the menu close when a menu link is clicked?
        // [ true | false ]
        close_on_click : true
      }
});

/* smooth scroll
 * snippet taken from
 * https://css-tricks.com/snippets/jquery/smooth-scrolling/
 */
$(function() {
  $('a[href*=#]:not([href=#])').click(function() {

    // if link clicked within off-canvas menu, close the menu
    if ($(".exit-off-canvas-link").length > 0) {
        $(".exit-off-canvas-link").on("click.toggleCanvas", function(){
              $(".exit-off-canvas").click();
            });
    }
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});


/* smooth sticky sidebar
 * taken from
 * http://stackoverflow.com/questions/2177983/how-to-make-div-follow-scrolling-smoothly-with-jquery
 */
$(function() {

    var element = $('.sticky-sidebar');

    // check if element is present
    if (element.length > 0) {
        var originalY = element.offset().top;

        // Space between element and top of screen (when scrolling)
        var topMargin = 20;

        // Should probably be set in CSS; but here just for emphasis
        element.css('position', 'relative');

        $(window).on('scroll', function(event) {
            var scrollTop = $(window).scrollTop();

            element.stop(false, false).animate({
                top: scrollTop < originalY
                        ? 0
                        : scrollTop - originalY + topMargin
            }, 700);
        });
    }
});


/*
 * owl carousel
 *
 */
$(document).ready(function() {

    var owl = $("#owl-example");

    // carousel setup
    owl.owlCarousel({
        navigation : false, // Show next and prev buttons
        slideSpeed : 300,
        pagination: false,
        paginationSpeed : 400,
        singleItem: true,
        transitionStyle:"fade",
        mouseDrag: false,
        touchDrag: false
    });

    // Custom Navigation Events
    $(".next").click(function() {
      owl.trigger('owl.next');
    });

    $(".prev").click(function() {
      owl.trigger('owl.prev');
    });
});