/*!
 * jQuery Sticky Footer 2.1
 * Corey Snyder
 * http://tangerineindustries.com
 *
 * Released under the MIT license
 *
 * Copyright 2013 Corey Snyder.
 *
 * Date: Thu Jan 22 2013 13:34:00 GMT-0630 (Eastern Daylight Time)
 * Modification for jquery 1.9+ Tue May 7 2013
 * Modification for non-jquery, removed all, now classic JS Wed Jun 12 2013
 * Modification for Foundation 5 auto height issues
 * Modification for new DOM change event listener
 * Modification for old IE mutation events, since not supported uses polling
 */

// get element by ID, not by tag name
var elementID = 'landing_page';

var MutationObserver = (function () {
    var prefixes = ['WebKit', 'Moz', 'O', 'Ms', '']
        for (var i=0; i < prefixes.length; i++) {
            if (prefixes[i] + 'MutationObserver' in window) {
                 return window[prefixes[i] + 'MutationObserver'];
            }
        }
        return false;
}());

window.onload = function() {
    stickyFooter();

    if (MutationObserver) {
        observer.observe(target, config);
    } else {
        //old IE
        setInterval(stickyFooter, 500);
    }
};

//check for changes to the DOM
var target = document.body;
var observer;
var config = { attributes: true, childList: true, characterData: true, subtree:true };

if (MutationObserver) {
    // create an observer instance
    observer = new MutationObserver(mutationObjectCallback);
}

function mutationObjectCallback(mutationRecordsList) {
    stickyFooter();
};


//check for resize event
$(window).on('resize', function() {
    stickyFooter();
});

// check for orientation change
$(window).on('orientationchange', function() {
    //$(window).trigger('resize');
    stickyFooter();
});

//var checkDOMInt = setInterval(stickyFooter, 500);


//lets get the marginTop for the elementID
function getCSS(element, property) {

  var elem = document.getElementById(element);
  var css = null;

  if (elem.currentStyle) {
    css = elem.currentStyle[property];

  } else if (window.getComputedStyle) {
    css = document.defaultView.getComputedStyle(elem, null).getPropertyValue(property);
  }

  return css;

}

function stickyFooter() {
    if (MutationObserver) {
        observer.disconnect();
    }
    document.body.setAttribute("style","height:auto");

    if (document.getElementById(elementID).getAttribute("style") != null) {
        document.getElementById(elementID).removeAttribute("style");
    }

    if (window.innerHeight != document.body.offsetHeight) {
        var offset = window.innerHeight - document.body.offsetHeight;
        //var offset = $(window).height() - $(document.body).height();
        //console.log('offset: '+offset);
        //console.log('innerHeight: '+window.innerHeight);
        //console.log('jQuery window height: '+$(window).height());
        //console.log('body.offsetHeight: '+document.body.offsetHeight);
        //console.log('jQuery body height: '+$(document.body).height());

        var current = getCSS(elementID, "margin-top");
        //console.log('current margin-top: '+current);

        if (isNaN(current)===true) {
            document.getElementById(elementID).setAttribute("style","margin-top:0px;");
            current = 0;
        } else {
            current = parseInt(current);
        }

        if (current+offset > parseInt(getCSS(elementID, "margin-top"))) {
            document.getElementById(elementID).setAttribute("style","margin-top:"+(current+offset)+"px;");
            //console.log('current+offset>margin-top, value:'+(current+offset));
        }

    }

    document.body.setAttribute("style","height:100%");

    //reconnect
    if (MutationObserver) {
        observer.observe(target, config);
    }
}

/*
! end sticky footer
*/