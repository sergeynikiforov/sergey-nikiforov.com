$(document).foundation({
    offcanvas : {
        // Should the menu close when a menu link is clicked?
        // [ true | false ]
        close_on_click : true
      }
});


// smart resize from Paul Irish
// http://www.paulirish.com/2009/throttled-smartresize-jquery-event-handler/
(function($,sr){

  // debouncing function from John Hann
  // http://unscriptable.com/index.php/2009/03/20/debouncing-javascript-methods/
  var debounce = function (func, threshold, execAsap) {
      var timeout;

      return function debounced () {
          var obj = this, args = arguments;
          function delayed () {
              if (!execAsap)
                  func.apply(obj, args);
              timeout = null;
          };

          if (timeout)
              clearTimeout(timeout);
          else if (execAsap)
              func.apply(obj, args);

          timeout = setTimeout(delayed, threshold || 100);
      };
  }
  // smartresize
  jQuery.fn[sr] = function(fn){  return fn ? this.bind('resize', debounce(fn)) : this.trigger(sr); };

})(jQuery,'smartresize');


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
          scrollTop: target.offset().top - 100
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

/*
$(function() {

    var sidebar = $('.sticky-sidebar');

    // check if element is present
    if (sidebar.length > 0) {
        var originalY = sidebar.offset().top;

        // Space between element and top of screen (when scrolling)
        var topMargin = 90;

        // Should probably be set in CSS; but here just for emphasis
        sidebar.css('position', 'relative');

        $(window).on('scroll', function(event) {
            var scrollTop = $(window).scrollTop();

            sidebar.stop(false, false).animate({
                top: scrollTop < originalY
                        ? 0
                        : scrollTop - originalY + topMargin
            }, 0);
        });
    }
});
*/


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
        url : "/contact/", // the endpoint
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


// change hero-image on photography page on hover
/*
$(document).ready(function() {
    var default_photo_bg_url = $('#change-bg-on-hover').css('background-image');
    $('.hover-background').hover(
       function(){
        var photo_bg_url = $(this).attr('id');
        $('#change-bg-on-hover').css("background-image", "url(\"" + photo_bg_url + "\")");
       },
       function(){
        $('#change-bg-on-hover').css("background-image", default_photo_bg_url);
       }
    );
});
*/

// waypoints use
var MyWaypoints = {};

MyWaypoints.changeTopBarFontColor = function () {
    $('#navigation-bar').toggleClass('black-color');
    $('#top-bar-sticky-page-header').toggleClass('black-color');
}

MyWaypoints.turnTopBarFontColorBlack = function () {
    $('#navigation-bar').addClass('black-color');
    $('#top-bar-sticky-page-header').addClass('black-color');
}

MyWaypoints.turnTopBarFontColorWhite = function () {
    $('#navigation-bar').removeClass('black-color');
    $('#top-bar-sticky-page-header').removeClass('black-color');
}


$(document).ready(function() {

    // toggle top-bar font color whatever it is
    MyWaypoints.waypointsToggleFontColor = $('.toggle-color').waypoint({
        handler: function(direction) {
            MyWaypoints.changeTopBarFontColor();
        },
        offset: 30
    });


    // on move down make top-bar font color black, on up - white
    MyWaypoints.waypointsFontColorBlack = $('.medium-toggle-color-black').waypoint({
        handler: function(direction) {
            if (window.innerWidth <= 1024 && window.innerWidth > 640) {
                if (direction == 'down') {
                    MyWaypoints.turnTopBarFontColorBlack();
                } else {
                    MyWaypoints.turnTopBarFontColorWhite();
                };
            };
        },
        offset: 40
    });

    // on down - white, on up - black
    MyWaypoints.waypointsFontColorWhite = $('.medium-toggle-color-white').waypoint({
        handler: function(direction) {
            if (window.innerWidth <= 1024 && window.innerWidth > 640) {
                if (direction == 'down') {
                    MyWaypoints.turnTopBarFontColorWhite();
                } else {
                    MyWaypoints.turnTopBarFontColorBlack();
                };
            }
        },
        offset: 40
    });

    // toggle hero-nav
    MyWaypoints.waypointsHeroNav = new Waypoint({
        element: document.getElementById('page-top'),
        handler: function(direction) {
            $('#hero-nav .page_header').animate({
                opacity: "toggle"
            }, 500);
            $('.landing').animate({
                opacity: "toggle"
            }, 500);
        },
        offset: -5
    });

    // refresh all waypoints using jquery mobile event
    $(window).on("orientationchange", function(event) {
        //console.log(event);
        Waypoint.refreshAll();
    });

    $(window).smartresize(function(event) {
        //console.log(event);
        Waypoint.refreshAll();
    });
});
