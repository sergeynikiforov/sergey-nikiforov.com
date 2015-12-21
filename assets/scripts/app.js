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
 * owl carousel
 *
 */
/*
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


// sticky sidebar on photoset page
var StickySidebar = {};

StickySidebar.isSetUp = false;
StickySidebar.isTopBarSetUp = false;
StickySidebar.isSidebarFixed = false;
StickySidebar.isSidebarBottom = false;

StickySidebar.changeTopBarBackgroundColor = function () {
    $('#top-bar-wrapper > div').toggleClass('white-bg');
    $('#top-bar-wrapper > .fixed').css('height', '70px');
}

StickySidebar.addTopBarBackgroundColor = function () {
    $('#top-bar-wrapper > div').addClass('white-bg');
    $('#top-bar-wrapper > .fixed').css('height', '70px');
}

StickySidebar.removeTopBarBackgroundColor = function () {
    $('#top-bar-wrapper > div').removeClass('white-bg');
    $('#top-bar-wrapper > .fixed').css('height', 'auto');
}

StickySidebar.setStickySidebarColumnHeight = function () {
    // sets sidebar wrapper column equal to thumbs height
    StickySidebar.thumbsHeight = $('#thumbs').outerHeight();
    $('#fixed-wrapper > div').outerHeight(StickySidebar.thumbsHeight);
}

StickySidebar.setStickySidebarColumnWidth = function () {

    // initial assingments
    if (StickySidebar.stickySidebarColumnWidth === undefined) {
        StickySidebar.sidebarLeftOffset = $('#sidebar-wrapper').offset().left;
        StickySidebar.stickySidebarColumnWidth = $('#fixed-wrapper > div').outerWidth();
        $('#fixed-wrapper > div').outerWidth(StickySidebar.stickySidebarColumnWidth);
    } else {
        // if sidebar is fixed
        if ($('.fixed-sidebar').length > 0) {
            StickySidebar.stickySidebarColumnWidth = parseInt($('#thumbs').css('margin-left'));
            $('#fixed-wrapper > div').outerWidth(StickySidebar.stickySidebarColumnWidth);
        } else {
            // if sidebar is not fixed
            $('#sidebar-wrapper').css('margin-left', '0px');
            StickySidebar.stickySidebarColumnWidth = $(window).innerWidth() - $('#thumbs').outerWidth();
            $('#fixed-wrapper > div').outerWidth(StickySidebar.stickySidebarColumnWidth);
        };
    }
}

StickySidebar.makeSidebarFixed = function() {
    $('#fixed-wrapper').addClass('fixed-sidebar');
    $('#thumbs-wrapper > div').addClass('large-offset-4');
    $('#sidebar-wrapper').removeClass('content-down');
    StickySidebar.isSidebarFixed = true;
}

StickySidebar.makeSidebarUnFixed = function() {
    $('#fixed-wrapper').removeClass('fixed-sidebar');
    $('#thumbs-wrapper > div').removeClass('large-offset-4');
    StickySidebar.isSidebarFixed = false;
}

StickySidebar.placeSidebarBottom = function() {
    $('#sidebar-wrapper').addClass('content-down');
    StickySidebar.isSidebarBottom = true;
}

StickySidebar.liftSidebarFromBottom = function() {
    $('#sidebar-wrapper').removeClass('content-down');
    StickySidebar.isSidebarBottom = false;
}

// function is called whenever we scroll or resize
StickySidebar.stickySidebar = function() {

    StickySidebar.makeFixedTop = $('#make-fixed').offset().top;
    StickySidebar.makeFixedBottom = $('#make-fixed').offset().top + $('#make-fixed').outerHeight();

    if (StickySidebar.isSidebarFixed) {
        // we touched the bottom
        if (StickySidebar.topbarBottom + StickySidebar.sidebarContentHeight > StickySidebar.makeFixedBottom) {
            StickySidebar.makeSidebarUnFixed();
            StickySidebar.placeSidebarBottom();
        }

        // we reached the top
        if (StickySidebar.topbarBottom < StickySidebar.makeFixedTop) {
            StickySidebar.makeSidebarUnFixed();
        };
    } else { // NOT fixed

        if (StickySidebar.isSidebarBottom) {
            if (StickySidebar.topbarBottom + StickySidebar.sidebarContentHeight < StickySidebar.makeFixedBottom) {
                StickySidebar.makeSidebarFixed();
                StickySidebar.liftSidebarFromBottom();
            };

        // sidebar NOT bottom
        } else {
            if (StickySidebar.topbarBottom > StickySidebar.makeFixedTop && StickySidebar.topbarBottom + StickySidebar.sidebarContentHeight < StickySidebar.makeFixedBottom) {
                StickySidebar.makeSidebarFixed();
            }
        };
    };
}

// set up top bar for sticky sidebar, depending on its position and viewport width
StickySidebar.setUpTopBar = function() {
    StickySidebar.topbarBottom = $('#top-bar-wrapper > div').offset().top + $('#top-bar-wrapper > div').outerHeight();
    StickySidebar.topbarMarker = $('#change-bg').offset().top + $('#change-bg').outerHeight();

    // set a non-transparent bg for large screens, otherwise - remove whatever color it was
    if (window.innerWidth > 1024) {

        // if it's lower than the mark - set new bg, else - remove color
        if (StickySidebar.topbarBottom >= StickySidebar.topbarMarker) {
            StickySidebar.addTopBarBackgroundColor();
            StickySidebar.isTopBarSetUp = true;
        } else {
            StickySidebar.removeTopBarBackgroundColor();
            StickySidebar.isTopBarSetUp = false;
        };
    } else {
        StickySidebar.removeTopBarBackgroundColor();
        StickySidebar.isTopBarSetUp = false;
    };

}


// called on ready & on resize
StickySidebar.setUpStickySidebar = function() {

    // set it only on large screens && on page with thumbs & sidebar-wrapper
    if ($('#sidebar-wrapper').length > 0 && $('#thumbs').length > 0 && window.innerWidth > 1024) {

        StickySidebar.sidebarContentHeight = $('#sidebar-wrapper').outerHeight();
        StickySidebar.setUpTopBar();
        StickySidebar.setStickySidebarColumnHeight();
        StickySidebar.setStickySidebarColumnWidth();
        StickySidebar.stickySidebar();

        StickySidebar.isSetUp = true;

    } else {
        StickySidebar.isSetUp = false;
    };
}


// toggle fixed class
/*
StickySidebar.waypointsMakeFixed = new Waypoint({
    element: document.getElementById('make-fixed'),
    handler: function(direction) {
        if (direction == 'down') {
            if (StickySidebar.topbarBottom < StickySidebar.sidebarBottom) {
                $('#fixed-wrapper').addClass('fixed-sidebar');
                $('#thumbs-wrapper > div').addClass('large-offset-4');
                $('#sidebar-wrapper').removeClass('content-down');
            };
            StickySidebar.changeTopBarBackgroundColor();
        } else {
            $('#fixed-wrapper').removeClass('fixed-sidebar');
            $('#thumbs-wrapper > div').removeClass('large-offset-4');
            StickySidebar.changeTopBarBackgroundColor();
        }
    }
});
*/

$(document).ready(function() {

    // when ready, try to set up sticky sidebar
    StickySidebar.setUpStickySidebar();

    // if sidebar is set up - listen for scroll events
    $(document).on('scroll', function() {
        if (StickySidebar.isSetUp == true) {
            StickySidebar.setUpTopBar();
            StickySidebar.setStickySidebarColumnHeight();
            StickySidebar.stickySidebar();
        };
    });

    // when resized - set up again
    $(window).on('resize', function() {
        StickySidebar.setUpStickySidebar();
        StickySidebar.setUpTopBar();
    });


    // toggle top-bar font color whatever it is
    MyWaypoints.waypointsToggleFontColor = $('.toggle-color').waypoint({
        handler: function(direction) {
            MyWaypoints.changeTopBarFontColor();
        },
        offset: 30
    });


    // on move down make top-bar font color black, on up - white
    MyWaypoints.waypointsFontColorBlack = $('.toggle-color-black').waypoint({
        handler: function(direction) {
            if (direction == 'down') {
                MyWaypoints.turnTopBarFontColorBlack();
            } else {
                MyWaypoints.turnTopBarFontColorWhite();
            };
        },
        offset: 40
    });

    // on down - white, on up - black
    MyWaypoints.waypointsFontColorWhite = $('.toggle-color-white').waypoint({
        handler: function(direction) {
            if (direction == 'down') {
                MyWaypoints.turnTopBarFontColorWhite();
            } else {
                MyWaypoints.turnTopBarFontColorBlack();
            };
        },
        offset: 40
    });

    // toggle hero-nav
    MyWaypoints.waypointsHeroNav = $('#page-top').waypoint({
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
});
