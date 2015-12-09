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
          scrollTop: target.offset().top - 10
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
        var topMargin = 90;

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


/*
 * AJAX contact me post
 * from https://realpython.com/blog/python/django-and-ajax-form-submissions/
 * + the code to handle csrf token
 */

$('#post-form').on('valid.fndtn.abide', function(event){
    event.preventDefault();
    contact_post();
});

function contact_post() {

    $.ajax({
        url : "/sn_app/contact", // the endpoint
        type : "POST", // http method
        data : {
            name    : $('#post-name').val(),
            email   : $('#post-email').val(),
            message : $('#post-message').val()
            }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-message').val(''); // remove the value from the input
            $('#post-name').val('');
            $('#post-email').val('');
            $('#post-result').prepend('<div data-alert id="post-result" class="my-alert-box" tabindex="0" aria-live="assertive" role="alertdialog">' + json.result + '<a tabindex="0" class="close" aria-label="Close Alert">&times;</a></div>');
            // reapply fndn listeners to alerts
            $(document).foundation('alert', 'reflow');
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#post-result').html('<div data-alert id="post-result" class="alert-box alert" tabindex="0" aria-live="assertive" role="alertdialog">' + json.result + '<a tabindex="0" class="close" aria-label="Close Alert">&times;</a></div>');
            // reapply fndn listeners to alerts
            $(document).foundation('alert', 'reflow');
             // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});